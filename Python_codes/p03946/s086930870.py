N,T = map(int,input().split())
A = list(map(int,input().split()))
dif = []
max_A = 0
for i in range(N):
    max_A = max(max_A,A[-1-i])
    dif.append(max_A-A[-1-i])
ans = 0
dif.sort(reverse=True)
for i in range(N-1):
    if dif[i]!=dif[i+1]:
        print(i+1)
        break