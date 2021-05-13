from itertools import product

n = int(input())
s = input()
ans = 0

for i in product(range(10), repeat = 3):
    a = s.find(str(i[0]))
    if a != -1 and a != n - 1:
        b = s[a + 1:].find(str(i[1]))
        if b != -1:
            b += a + 1
            if b != n - 1:
                c = s[b + 1:].find(str(i[2]))
                if c != -1:
                    ans += 1
print(ans)