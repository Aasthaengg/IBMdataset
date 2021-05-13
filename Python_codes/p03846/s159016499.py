from collections import Counter

n = int(input())
a = list(map(int,input().split()))
c = Counter(a)
m = c.most_common()
judge = 0
ans = 1
if n%2 == 0:
    for i in range(len(m)):
        if m[i][0]%2==0 or m[i][1]!=2 or m[i][0]>n-1:
            judge = 1
    num=n//2
else:
    for i in range(len(m)):
        if (m[i][0]==0 and m[i][1]!=1) or m[i][0]%2==1 or (m[i][1]!=2 and m[i][0]!=0)or m[i][0]>n-1:
            judge = 1
    num=(n-1)//2
if judge ==1:
    print('0')
else:
    for i in range(num):
        ans=ans*2%1000000007
    print(ans)
