n = int(input())
s = [int(input()) for _ in range(n)]
total = sum(s)
s.sort()
cnt = 0
if total % 10 == 0:
    for i in s:
        if i % 10 != 0:
            total -= i
            break
        else:
            cnt += 1
if cnt == n:
    print(0)
else:
    print(total)