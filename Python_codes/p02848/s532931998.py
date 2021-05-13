n = int(input())
s = input()

ans = ''
for si in s:
    num = ord(si)+n
    if num > ord('Z'):
        ans += chr(num-26)
    else:
        ans += chr(num)
print(ans)
