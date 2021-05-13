n = int(input())
p = list(map(int,input().split()))

q = [(i+1) for i in range(n)]
cnt = 0
for i in range(n):
    if p[i]!=q[i]:
        cnt +=1
if cnt >2:
    print("NO")
else:
    print("YES")