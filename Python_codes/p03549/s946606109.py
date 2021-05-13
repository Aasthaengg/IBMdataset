n,m = map(int,input().split())
s = 0
a = m*1900+(n-m)*100
t = 2**m
print(a*t)