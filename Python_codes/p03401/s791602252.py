from itertools import accumulate
n = int(input())
a = [0]+list(map(int,input().split()))+[0]
s = [abs(a[i]-a[i+1]) for i in range(n+1)]
s = sum(s)
for i in range(1,n+1):
    print(s+abs(a[i-1]-a[i+1])-(abs(a[i-1]-a[i])+abs(a[i]-a[i+1])))