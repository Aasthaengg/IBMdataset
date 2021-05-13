import collections
N = int(input())
a = [int(input()) for i in range(N)]
c=collections.Counter(a)
cnt=0
for i in c:
    if c[i]%2==1:
        cnt+=1
print(cnt)