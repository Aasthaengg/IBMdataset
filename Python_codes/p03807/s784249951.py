N = int(input())
A = list(map(int,input().split()))
cnt = 0
for Ai in A:
    cnt += Ai%2
if(cnt%2==0):
    print("YES")
else:
    print("NO")