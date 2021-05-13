n, k = map(int, input().split())
data = list(map(int, input().split()))
mod = 10**9 + 7

invs = []
for idx in range(n):
    result = [0,0]
    for idx2 in range(n):
        if idx2 < idx:
            loc = 1
        elif idx2 > idx:
            loc = 0
        else:
            continue
        if data[idx2] < data[idx]:
            result[loc] += 1
    invs.append(result)
ans = 0
for aft, bef in invs:
    ans += aft*k
    m = (bef+aft)*(k-1)
    ans += (m*k)//2
print(ans%mod)
