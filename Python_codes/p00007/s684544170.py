n=int(input())
a=100000
for i in range(n):
    a*=1.05
    if a%1000 !=0:
        a=(a//1000)*1000+1000
print(int(a))
