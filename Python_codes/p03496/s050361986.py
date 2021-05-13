n=int(input())
a=[int(j) for j in input().split()]
maxind=a.index(max(a))+1
minind=a.index(min(a))+1
if min(a)>0:
    print(n-1)
    for i in range(1,n):
        print(i,i+1)
else:
    if max(a)<0:
        print(n-1)
        for i in range(1,n)[::-1]:
            print(i+1,i)
    else:
        if max(a)+min(a)>0:
            ans=[]
            for i in range(n):
                if a[i]<0:
                    ans.append(i+1)
            print(len(ans)+n-1)
            for i in ans:
                print(maxind,i)
            for i in range(1,n):
                print(i,i+1)
        else:
            ans=[]
            for i in range(n):
                if a[i]>0:
                    ans.append(i+1)
            print(len(ans)+n-1)
            for i in ans:
                print(minind,i)
            for i in range(1,n)[::-1]:
                print(i+1,i)
            






