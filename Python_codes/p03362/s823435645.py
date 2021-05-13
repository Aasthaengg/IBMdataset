#096_D
n = int(input())
prime_5 = []
for i in range(2, 55556):
    flg = (i % 5 == 1)
    if flg:
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                flg = False
                break
    if flg:
        prime_5.append(i)
print(*prime_5[:n])