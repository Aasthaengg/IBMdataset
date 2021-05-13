n = int(input())
t,a= map(int,input().split())
h = list(map(int,input().split()))
tp = 1
near = abs(t-h[0]*0.006 - a)
for i in range(1,n):
    if abs(t-h[i] * 0.006 - a) < near:
        near = abs(t-h[i] * 0.006 - a)
        tp = i+1
print(tp)
    
