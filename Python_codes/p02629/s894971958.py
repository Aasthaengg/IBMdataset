N = int(input())

ans = ""
temp = N
while temp > 0:
    temp -= 1
    ans += chr(temp % 26 + ord('a'))
    temp = temp // 26

print(ans[::-1])
