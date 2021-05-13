n = int(input())

left = 1
right = n
cnt = []
while n % 2 == 0:
    n //= 2
    cnt.append(2)

f = 3
while f * f <= n:
    if n % f == 0:
        n //= f
        cnt.append(f)
    else:
        f += 2

cnt.append(n)

for i in range(len(cnt)):
    left *= cnt[i]
    right //= cnt[i]
    if left < 10 and right < 10:
        print('Yes')
        exit()
print('No')