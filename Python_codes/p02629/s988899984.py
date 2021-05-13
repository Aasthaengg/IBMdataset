
def num2alpha(num):
    return chr(num+65).lower()


N = int(input()) - 1
ans = ""
while(True):
    surplus = N % 26
    N -= surplus
    num = surplus
    ans = num2alpha(num) + ans
    if N == 0:
        break
    else:
        N //= 26
        N -= 1
print(ans)