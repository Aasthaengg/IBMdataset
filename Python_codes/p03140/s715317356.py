n=int(input())
a=list(input())
b=list(input())
c=list(input())
cnt=0
for i in range(n):
    if a[i]==b[i]==c[i]:
        continue
    if a[i]==b[i] or b[i]==c[i] or a[i]==c[i]:
        cnt+=1
    else:
        cnt+=2
print(cnt)