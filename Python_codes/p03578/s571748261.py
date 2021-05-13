n=int(input())
d=sorted(list(map(int,input().split())))
m=int(input())
t=sorted(list(map(int,input().split())))
if m>n:
    print("NO")
else:
    a=0
    for i in range(m):
        flag=0
        while flag!=1:
            if a==n:
                print("NO")
                exit()
            if t[i]>d[a]:
                a+=1
            elif t[i]==d[a]:
                a+=1
                flag=1
            else:
                print("NO")
                exit()
    print("YES")
