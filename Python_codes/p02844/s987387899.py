N = int(input())
S = input()

ret = 0
for x in range(10):
    for y in range(10):
        for z in range(10):
            a = S.find(str(x))
            if a != -1:
                b = S.find(str(y), a + 1)
                if b != -1:
                    c = S.find(str(z), b + 1)
                    if c != -1:
                        ret += 1
print(ret)