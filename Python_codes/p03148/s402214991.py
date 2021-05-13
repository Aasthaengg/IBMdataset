from collections import deque
n,k = map(int,input().split())
ans = 0
ansl = []
sushi = []
sushi1 = deque()
sushi2 = []
various = [0 for i in range(n)]
v = 0
for i in range(n):
    td = list(map(int,input().split()))
    sushi.append(td)
sushi.sort(key=lambda x:x[1],reverse=True)
for i in range(n):
    if i < k:
        ans += sushi[i][1]
        if various[sushi[i][0]-1] == 0:
            v += 1
        various[sushi[i][0]-1] += 1
        sushi1.append(sushi[i])
    else:
        sushi2.append(sushi[i])
ansl.append(ans+v*v)
for i in range(n-k):
    if various[sushi2[i][0]-1] == 0:
        key = 0
        while key < 1 and len(sushi1) > 0:
            a,b = sushi1.pop()
            if various[a-1] > 1:
                key += 1
                various[a-1] -= 1
        if key > 0:
            various[sushi2[i][0]-1] += 1
            ans = ans + sushi2[i][1] - b
            v += 1
            ansl.append(ans+v*v)
print(max(ansl))