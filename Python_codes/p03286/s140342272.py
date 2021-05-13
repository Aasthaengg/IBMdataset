n = int(input())
# したから計算
if n == 0:
    print(0)
    exit()
ans = ""
digit = 1
while n != 0:
    num = 0
    if n % pow(2, digit):
        num = 1
    ans = str(num) + ans
    n -= num * pow(-2, digit - 1)
    digit += 1
print(ans)
