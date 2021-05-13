n = int(input())
if n ==0:
    print(0)
else:
    res = []
    while n != 0:
        if n % 2 == 1:
            res.append("1")
        else:
            res.append("0")
        n = (n-n%2) // -2
    res = res[::-1]
    print("".join(res))
