from collections import Counter
n=int(input())
a=list(map(int,input().split()))
b=Counter(a)
c=len(([i[0] for i in b.items() if i[1] == 2]))
if n%2==0:
    if n//2==c:
        print(2**(len(set(a)))%1000000007)
    else:
        print(0)
else:
    if (n-1)//2==c and a.count(0)==1:
        print(2**(len(set(a))-1)%1000000007)
    else:
        print(0)
