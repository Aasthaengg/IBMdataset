N, M = map(int, input().split())

L = list()
R = list()
for i in range(M):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

maxL = max(L)
minR = min(R)

num = 0 
for j in range(maxL,minR+1):
    num +=1

print(num)