import sys
 
stdin = sys.stdin
 
ni = lambda:int(ns())
na = lambda:list(map(int,stdin.readline().split()))
ns = lambda:stdin.readline().rstrip()  # ignore trailing spaces

N = ni()
answer = 0
cur = 1
while cur * (cur + 2) <= N:
    y = N - cur
    if y % cur != 0:
        cur += 1
        continue
    x = y // cur
    if x > cur:
        #print(cur)
        answer += x
    cur += 1
print(answer)