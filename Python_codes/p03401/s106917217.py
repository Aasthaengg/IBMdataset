n=int(input())
a=[0]+list(map(int,input().split()))+[0]

al=0
#print(a)

for i in range(n+1):
    al+=abs(a[i]-a[i+1])

for j in range(n):
    t=(abs(a[j]-a[j+1])+abs(a[j+1]-a[j+2]))-(abs(a[j]-a[j+2]))
    print(al-t)