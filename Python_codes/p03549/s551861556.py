n,m = map(int,input().split())
a = 1
for i in range(m):
    a*=2
b = 1900*m+100*(n-m)
print(a*b)