h,w,k=map(int,input().split())
s=[list(input())for i in range(h)]
a=[[0]*w for i in range(h+1)]
b=1
for i in range(h):
    if "#" in s[i]:
        for j in range(w):
            a[i+1][j]=str(b)
            if s[i][j]=="#" and "#" in s[i][j+1:]:
                b+=1
        b+=1
        if a[i][0]==0:
            f=i
            while a[f][0]==0:
                a[f]=a[f+1]
                f-=1
                if f<=0:
                    break
    else:
        a[i+1]=a[i]
for i in range(1,h+1):
    print(*a[i])