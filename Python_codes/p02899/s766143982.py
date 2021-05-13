N = int(input())
a = list(map(int, input().split()))
rev = [0]*N
for i in range(N):
    rev[a[i] - 1] = i +1
for i in range(N):
    print(rev[i], end=" ")