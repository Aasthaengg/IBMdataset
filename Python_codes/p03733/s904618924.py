n,t = map(int,input().split())
x = list(map(int,input().split()))
m = 0

for i in range(1,n):
    if x[i] - t <= x[i - 1]:
        m += x[i] - x[i - 1]
    else:
        m += t
    

print(m + t)