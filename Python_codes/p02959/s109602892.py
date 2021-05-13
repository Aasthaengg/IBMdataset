n=int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
mosters=sum(a)

for i in range(n):
    hunted1 = min(a[i],b[i])
    a[i] -=hunted1
    b[i] -=hunted1
    hunted2 = min(a[i+1],b[i])
    a[i+1] -=hunted2
    b[i] -=hunted2
    
print(mosters-sum(a))