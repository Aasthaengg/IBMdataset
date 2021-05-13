N = int(input())
A = list(map(int, input().split(' ')))
fusion = sum(A)
ans = 1
A.sort()

for i in range(N - 2, -1, -1):
    fusion -= A[i + 1]
    if fusion * 2 >= A[i + 1]:
        ans += 1
    else:
        break

print(ans)