n = int(input())
a = list(map(int, input().split()))

ruiseki_add = [0] * (n + 1)
for i in range(n):
    ruiseki_add[i + 1] = ruiseki_add[i] + a[i]

ruiseki_xor = [0] * (n + 1)
for i in range(n):
    ruiseki_xor[i + 1] = ruiseki_xor[i] ^ a[i]
    
def solve(s, mid):
    xor_sum = ruiseki_add[mid + 1] - ruiseki_add[s] 
    add_sum = ruiseki_xor[mid + 1] ^ ruiseki_xor[s]
    if xor_sum == add_sum:
        return True
    else:
        return False

ans = 0
for i in range(n):
    ok = i
    ng = n
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if solve(i, mid):
            ok = mid
        else:
            ng = mid
    ans += ng - i
print(ans)