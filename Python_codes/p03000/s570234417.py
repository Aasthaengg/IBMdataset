n,x = map(int, input().split())
L = list(map(int, input().split()))
l = [0]
cnt = 1
for i in range(n):
    l.append(l[-1]+L[i])
    if l[-1] <= x: cnt += 1
    else: break
print(cnt)