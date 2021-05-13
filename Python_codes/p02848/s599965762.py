n = int(input())
s = input()
ans = ""
for i in range(len(s)):
    num = ord(s[i])
    if num + n > 90:
        num1 = (num+n)-90+64
    if num + n <= 90:
        num1 = num + n
    ans += chr(num1)
print(ans)