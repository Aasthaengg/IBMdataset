import collections
n=int(input())
a= list(map(int, input().split()))

mod = 10**9+7
c = collections.Counter(a)
c =c.most_common()
c.sort()

if n%2==0:
    for i in range(len(c)):
        if c[i][0]==i*2+1 and c[i][1]==2:
            continue
        else:
            print(0)
            exit()
    ans=pow(2,n//2,mod)
    print(ans)

else:
    for i in range(len(c)):
        if i==0:
            if c[i][0]==0 and c[i][1]==1:
                continue
            else:
                print(0)
                exit()
        else:
            if c[i][0] == i * 2 and c[i][1] == 2:
                continue
            else:
                print(0)
                exit()
    ans=pow(2,n//2,mod)
    print(ans)