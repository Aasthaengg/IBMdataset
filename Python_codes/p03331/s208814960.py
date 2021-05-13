N = int(input())
ans = float("inf")
for i in range(1,N):
    if sum(map(int, str(i))) + sum(map(int, str(N-i))) < ans:
        ans = sum(map(int, str(i))) + sum(map(int, str(N-i)))
print(ans)