X = input()
Tnum = len(X) // 2
Snum = len(X) // 2
num = 0
ans = 0
for i in X:
    if i == 'T':
        num -= 1
        Tnum -= 1
    else:
        num += 1
        Snum -= 1

    if num < 0:
        ans += 1
        num = 0
print(ans*2)