n=int(input())
s=100000
for i in range(n):
    s=s*(1+5/100)
    s=-(-s//1000)
    s=s*1000
print(int(s))
