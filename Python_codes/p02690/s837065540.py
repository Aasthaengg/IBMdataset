x = int(input())

s = []
for i in range(300):
    j = i ** 5
    s.append(j)
    s.append(-1*j)

for a in s:
    for b in s:
        ans = a - b
        if ans == x:
            if a >= 0:
                aa = int(a ** (1/5))
            else:
                aa = int(abs(a) ** (1/5)) * -1
            if b >= 0:
                bb = int(b ** (1/5))
            else:
                bb = int(abs(b) ** (1/5)) * -1
            print(aa,bb)
            exit()
