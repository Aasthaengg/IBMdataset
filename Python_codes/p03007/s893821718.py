N = int(input())
A = list(map(int,input().split()))
ans = []
A.sort()
a = A.pop(0)
b = A.pop()
N -= 2
k = 1
for i in range(N):
    y = A.pop()
    if y<0:k=0
    if k:
        ans.append([a,y])
        a -= y
    else:
        ans.append([b,y])
        b -= y
ans.append([b,a])
print(b-a)
for a in ans: print(*a)