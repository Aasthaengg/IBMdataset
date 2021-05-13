d, g = map(int, input().split())
pc = []
for _ in range(d):
    p, c = map(int, input().split())
    pc.append((p, c))
ans = 1000
for i in range(2**d):
    score = 0
    k = 0
    for j in range(d):
        if i>>j&1:
            score += pc[j][0]*100*(j+1) + pc[j][1]
            k += pc[j][0]
    if score>=g:
        ans = min(ans, k)
        continue
    for j in range(d-1, -1, -1):
        if i>>j&1:
            continue
        if score+(pc[j][0]-1)*100*(j+1)<g:
            score += (pc[j][0]-1)*100*(j+1)
            k += pc[j][0]-1
            continue
        k += (g-score+100*(j+1)-1)//(100*(j+1))
        ans = min(ans, k)
        break
print(ans)