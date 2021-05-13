n=int(input())
a=list(map(int,input().split()))
a.insert(0,0)   #最初に0
a.insert(n+1,0) #最後に0

res = sum([abs(a[i]-a[i+1]) for i in range(n+1)]) #階差の和

for i in range(1,n+1):
    tmp = res + abs(a[i-1]-a[i+1]) - (abs(a[i-1]-a[i]) + abs(a[i]-a[i+1]))
    print(tmp)