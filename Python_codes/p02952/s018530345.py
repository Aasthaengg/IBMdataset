n = int(input())
# 100000
# 1-9 9 100-999 900 10000-99999 90000
if n <= 9:
    print(n)
    exit()
if n > 9 and n <= 999:
    print(9 + max(n-99,0))
    exit()
if n > 999 and n <= 99999:
    print(9 + 900 + max(n-9999,0))
    exit()
if n > 99999 :
    print(9 + 900 + 90000)
    exit()