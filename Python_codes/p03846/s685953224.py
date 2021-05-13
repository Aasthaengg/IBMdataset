n = int(input())
a = list(map(int, input().split()))

mod = 10 ** 9 + 7

cnt = [0] * n
for v in a:
    cnt[v] += 1

res = 1

if n % 2 == 1:
    if cnt[0] != 1:
        print(0)
        exit()
    
    for i in range(1, n):
        if i % 2 == 1:
            if cnt[i] > 0:
                print(0)
                exit()
        else:
            if cnt[i] == 2:
                res = res * 2 % mod
            else:
                print(0)
                exit()
    
else:
    for i in range(1, n):
        if i % 2 == 0:
            if cnt[i] > 0:
                print(0)
                exit()
        else:
            if cnt[i] == 2:
                res = res * 2 % mod
            else:
                print(0)
                exit()

print(res)