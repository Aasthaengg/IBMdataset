N, D = map(int, input().split())
cnt = 1

while N-2*D-1>0:
    cnt += 1
    N -= 2*D+1

print(cnt)