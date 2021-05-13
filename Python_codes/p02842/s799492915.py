n = int(input())
x = int(n / 1.08)

while int(x*1.08) <= n:
    if int(x*1.08) == n:
        print(x)
        break
    else:
        x += 1

if int(x*1.08) > n:
    print(":(")