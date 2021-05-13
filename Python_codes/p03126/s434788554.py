n,m = map(int,input().split())


menu =[0]*m 
for i in range(n):
    k,*a = map(int,input().split())
    for j in range(k):
        menu[a[j]-1] += 1

print(menu.count(n))