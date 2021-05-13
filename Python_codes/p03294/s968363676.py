n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    c+=i-1
print(c)