def num2alpha(num):
    if num <= 26:  return chr(64 + num)
    elif num % 26 == 0:  return num2alpha(num // 26 - 1) + chr(90)
    return num2alpha(num // 26) + chr(64 + num % 26)

N = int(input())
ans = num2alpha(N).lower()
print(ans)