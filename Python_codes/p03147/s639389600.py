import sys
input = sys.stdin.readline

N = int(input())
h =[0] + list(map(int,input().split()))
ans = 0
for i in range(len(h)-1):
    ans += max( h[i+1]-h[i],0)
print(ans)