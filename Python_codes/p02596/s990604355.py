k = int(input())
n = 7

cnt = 1

for i in range(k):
    if n % k == 0:
        break
    n = (n*10 + 7) % k
    cnt += 1

if n % k == 0:
    print(cnt)
else:
    print(-1)
    

