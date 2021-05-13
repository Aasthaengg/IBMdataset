n=int(input())
d=list(map(int,input().split()))
m=int(input())
t=list(map(int,input().split()))
count=0
if m>n:
    print("NO")
else:
    d.sort()
    t.sort()
    for i in range(n):
        if count==m:
            break
        if t[count]==d[i]:
            count+=1
    if count==m:
        print("YES")
    else:
        print("NO")
