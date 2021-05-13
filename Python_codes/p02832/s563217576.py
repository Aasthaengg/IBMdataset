n = int(input())
l = list(map(int, input().split()))
j = 1
for i in l:
    if i==j: j+=1
if j==1:print(-1)
else:print(n-j+1)