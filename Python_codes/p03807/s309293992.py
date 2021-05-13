n=int(input())
a=list(map(int,input().split()))
o=0
for x in a:
    if x%2!=0:o+=1
if o%2==1:print("NO")
else:print("YES")