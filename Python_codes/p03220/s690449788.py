n = int(input())
t, a = map(int,input().split())
h = list(map(int,input().split()))
s = 0
d = t-a
m = abs(d - h[0]*0.006)
for i in range(1,n):
    if m > abs(d - h[i]*0.006):
        s = i
        m = abs(d - h[i]*0.006)
print(s+1)