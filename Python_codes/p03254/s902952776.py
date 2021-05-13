N, x = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)

if sum(A) < x:
    print(N-1)
    exit()

A = [1] + A
ans = 0
while A[-1] <= x:
    x -= A[-1]
    A.pop()
    ans += 1
print(ans)