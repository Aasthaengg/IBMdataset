N = int(input())
robots = [tuple(map(int,input().split())) for _ in range(N)]
 
robots = [(x+l,x-l) for x,l in robots]
 
robots.sort()
 
cnt = 0
last = -float('inf')
for r,l in robots:
    if last <= l:
        cnt += 1
        last = r
 
print(cnt)