s=list(input())
m=len(s)
a=[0]*(m+1)
add=1
for i in range(m):
    if s[i]=="<":
        a[i+1]+=add
        add+=1
    else:
        add=1
for i in range(m-1,-1,-1):
    if s[i]==">" and a[i]<=a[i+1]:
        a[i]+=a[i+1]-a[i]+1
print(sum(a))