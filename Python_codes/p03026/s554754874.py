N = int((input()))
ab = [list(map(int,input().split())) for _ in range(N-1)]
c = list(map(int,input().split()))
c.sort(reverse = True)

al = [[] for _ in range(N+1)]
for a,b in ab:
    al[a].append(b)
    al[b].append(a)

d = [0] * (N)
d[ab[0][0]-1] = c[0]
cnt = 1
child = al[ab[0][0]]
ans = 0
Check = [True] * (N+1)
Check[ab[0][0]] = False

while child and cnt < N:
    pi = int(child.pop())
    Check[pi] = False
    d[pi-1] = (c[cnt])
    ans += c[cnt]
    for i in al[pi]:
        if Check[i]:child.append(i)
    cnt += 1
    
print(ans)
print(' '.join(map(str,d)))
