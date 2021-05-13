import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int,input().split()))

target = 1
cnt = 0

for i in range(N-1):
    if a[i] == target:
        target += 1
    else:
        cnt +=1
if target == a[-1]:
    print(cnt)
elif target==1 and a[-1] != 1:
    print(-1)
else:
    print(cnt+1)
