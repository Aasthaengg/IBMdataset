N = int(input())
cnt = 0
for n in range(1,N + 1):
    l = len(str(n))
    if l % 2 == 1:
        cnt += 1

print(cnt)