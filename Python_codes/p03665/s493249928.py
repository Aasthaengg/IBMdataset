n, p = map(int, input().split())
a = list(map(int, input().split()))
cnt = [0] * 2
for num in a:
    cnt[num % 2] += 1

if cnt[1] == 0:
    if p == 0:
        print(2 ** n)
    else:
        print(0)

else:
    print(2 ** ( n - 1))
