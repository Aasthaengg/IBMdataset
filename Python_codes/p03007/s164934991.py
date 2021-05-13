n=int(input())
a=list(map(int,input().split()))
a.sort()
hu=0
for b in a:
    if b<0:
        hu+=1
    else:
        break
if hu==0:
    hu=1
if hu==n:
    hu=n-1
ansl=[]
nowl=a[0]
for i in range(hu,n-1):
    ansl.append((nowl,a[i]))
    nowl-=a[i]

nowr=a[n-1]
for i in range(1,hu):
    ansl.append((nowr,a[i]))
    nowr-=a[i]

ansl.append((nowr,nowl))
print(nowr-nowl)
for i in range(n-1):
    x,y=ansl[i]
    print(x,y)
