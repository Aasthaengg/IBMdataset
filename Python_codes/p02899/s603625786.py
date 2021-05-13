N = int(input())
A = list(map(int, input().split()))
time = [0 for i in range(N)]

for i in range(N):
    time[A[i]-1] = i+1

for j in range(N):
    print(time[j],end=" ")