import sys
A, B = map(int, input().split())

if B == 1:
    print(0)
    sys.exit(0)
cnt = 1
while True:
    if A*cnt+1-cnt >= B:
        break
    cnt += 1

print(cnt)