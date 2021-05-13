n = int(input())
MOD = 10 ** 9 + 7

a = list(map(int, input().split()))
a.sort()

if n % 2 == 1:
    for i in range(n):
        if i % 2 == 1 and a[i] - 1 == i: continue
        elif i % 2 == 0 and a[i] == i: continue
        else: 
            print(0)
            exit()
else:
    for i in range(n):
        if i % 2 == 1 and a[i] == i: continue
        elif i % 2 == 0 and a[i] - 1 == i: continue
        else: 
            print(0)
            exit()

print(2 ** (n//2) % MOD)