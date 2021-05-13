n = int(input())
a = list(map(int,input().split()))
c = 0
for i in range(1,n-1):
    if(a[i] == a[i-1]):
        a[i] = a[i+1]+1
        c += 1
if(a[-1] == a[-2]):c+=1
print(c)