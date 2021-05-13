
N, = map(int, input().split())
R = 0
for i in range(1, N+1):
    R += (N-1)//i
print(R)
