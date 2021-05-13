N = int(input())
A = list(map(int,input().split()))
ans = 0

for i in range(N):
    if i == 0:
        a = A[i]
        count = 1
    else:
        if a == A[i]:
            count += 1
            continue
        else:
            ans += count // 2
            a = A[i]
            count = 1
ans += count // 2
print(ans)
