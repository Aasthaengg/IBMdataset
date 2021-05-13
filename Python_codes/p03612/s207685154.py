N = int(input())
P = list(map(int,input().split()))
count = 0
for i in range(N):
    if i != N-1 and P[i] == i+1:
        P[i],P[i+1]=P[i+1],P[i]
        count += 1
if P[N-1] == N:
    count += 1
print(count)