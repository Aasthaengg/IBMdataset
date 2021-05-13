N = int(input())
lower = []
upper = []
for i in range(N):
    a, b = map(int, input().split())
    lower.append(a)
    upper.append(b)
lower.sort()
upper.sort()
if N % 2 == 1:
    print(upper[(N-1)//2]-lower[(N-1)//2]+1)
else:
    print(upper[N//2]+upper[N//2 - 1]-lower[N//2]-lower[N//2 - 1]+1)