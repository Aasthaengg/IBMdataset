s = input()
ls = [0 for i in range(len(s))]
a = []
cur = 'R'
for x in s[1:]:
    if cur[-1] == x:
        cur += x
    else:
        a.append(cur)
        cur = x
a.append(cur)
num = 0
for i, x in enumerate(a):
    if i%2 == 0:
        ls[len(x)-1+num] += len(x) - len(x)//2
        ls[len(x)+num] += len(x)//2
        num += len(x)
    else:
        ls[num] += len(x) - len(x)//2
        ls[num-1] += len(x)//2
        num += len(x)
print(*ls)