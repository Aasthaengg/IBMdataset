N = int(input())
A = list(map(int, input().split()))
ans = 0
while True:
    if all(A[i]%2==0 for i in range(N)):
        A = [A[i]//2 for i in range(N)]
        ans += 1
    else:
        break

print(ans)