n = int(input())
s = input()
t = input()

for i in range(n, 2 * n):
    check = 2 * n - i
    ss = s[-1 * check:]
    tt = t[:check]
    if ss == tt:
        print(i)
        exit()

print(2 * n)
