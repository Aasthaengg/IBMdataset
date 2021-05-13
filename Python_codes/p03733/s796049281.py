N,T=map(int,input().split())
Time=list(map(int,input().split()))

interval=[]
for i in range(N-1):
    if Time[i+1]-Time[i]>T:
        interval.append(Time[i+1]-Time[i])

k=len(interval)
print(Time[-1]+T-(sum(interval)-k*T))