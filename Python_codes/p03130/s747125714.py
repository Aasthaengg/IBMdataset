from collections import deque
S = [list(map(int, input().split())) for _ in range(3)]

l=[0,0,0,0]

for i in range(3):
    for j in range(2):
        l[S[i][j]-1]+=1
#print(l)
if max(l)==3:
    print("NO")
else:
    print("YES")