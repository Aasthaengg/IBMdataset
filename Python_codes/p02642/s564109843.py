N = int(input())
A = list(map(int, input().split()))
A.sort()
B = [0] * (10**6+1)
ans = 0
for a in A:
    if B[a] == 0:
        ans += 1
        B[a] = 2
        tmp = 2*a
        while tmp <= 10**6:
            B[tmp] = 1
            tmp += a
    elif B[a] == 2:
        B[a] = 1
        ans -= 1
print(ans)