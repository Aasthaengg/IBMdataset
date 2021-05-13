n = int(input())
a = [int(x) for x in input().split()]

money=1000
kabukosuu=0

for i in range(n-1):
    money+=kabukosuu*a[i]
    kabukosuu=0
    if a[i]<a[i+1]:
        kabukosuu=money//a[i]
        money=money%a[i]
    
money+=kabukosuu*a[n-1]

print(money)