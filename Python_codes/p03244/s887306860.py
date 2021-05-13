import collections
n=int(input())
v=list(map(int,input().split()))
c1=collections.Counter(v[::2])
c2=collections.Counter(v[1::2])
c1_v1=c1.most_common()[0][0]
c2_v1=c2.most_common()[0][0]
c1_n1=c1.most_common()[0][1]
c2_n1=c2.most_common()[0][1]

if c1_v1!=c2_v1:
    print(n-c1_n1-c2_n1)
else:
    if c1_n1==n//2:
        if c2_n1==n//2:
            print(n//2)
        else:
            c2_n2=c2.most_common(2)[1][1]
            print(n-c1_n1-c2_n2)
    else:
        c1_n2=c1.most_common(2)[1][1]
        if c2_n1==n//2:
            print(n-c1_n2-c2_n1)
        else:
            c2_n2=c2.most_common(2)[1][1]
            print(min(n-c1_n2-c2_n1,n-c1_n1-c2_n2))
