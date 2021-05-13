from collections import deque
n = int(input())
p = [[0 for i in range(10)] for j  in range(10)]
for i in range(1,10):
    for j in range(1,10):
        if i == j:
            if i <= n:
                p[i][j] += 1
        now = ""
        d = deque()
        d.append("")
        while d:
            now = d.popleft()
            for k in range(10):
                d.append(now+str(k))
            if int(str(i) + now + str(j)) <= n:
                p[i][j] += 1
            else:
                break
ans = 0            
    
for i in range(1,10):
    for j in range(1,10):
        ans += p[i][j]*p[j][i]

print(ans)