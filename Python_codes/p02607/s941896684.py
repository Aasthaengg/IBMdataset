n=int(input())
a=input().split()
cnt=0
for i in range(0,n,2):
    if(int(a[i])%2!=0):
        cnt=cnt+1
print(cnt)
