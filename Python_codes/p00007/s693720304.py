a=100000
n=int(input())
for i in range(n):
    a*=1.05
    if a%1000:
        a=int(a//1000*1000+1000)
print(a)
