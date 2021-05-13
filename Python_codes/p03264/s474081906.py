k = int(input())

p = k // 2

if k % 2 == 0:
    print(p * p)
elif k % 2 > 0:
    print(p*(p+1))