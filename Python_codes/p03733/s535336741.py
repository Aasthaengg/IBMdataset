#ABC073-C
n,t = map(int,input().split())
time = list(map(int,input().split()))

cnt = t

for i in range(1,n):
    if time[i] - time[i-1] <= t:
        cnt += time[i] - time[i-1]
    else:
        cnt += t
        
print(cnt)