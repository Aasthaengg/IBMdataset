n= int(input())
a = list(map(int,input().split()))
c=0
for i in range(n):
    if a[i]%2==1:
        c+=1
print("YES" if c%2==0 else "NO")