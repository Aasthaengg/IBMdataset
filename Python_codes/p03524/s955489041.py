s = input()
chars = [0, 0, 0]

for i in range(len(s)):
    if s[i] == "a":
        chars[0] += 1
    elif s[i] == "b":
        chars[1] += 1
    else:
        chars[2] += 1

chars = sorted(chars)

if chars[0] == chars[1]:
    if chars[1] == chars[2]:
        print("YES")
    elif chars[2] == chars[1] + 1:
        print("YES")
    else:
        print("NO")
elif (chars[1] == chars[2]) and (chars[0] == chars[1] - 1):
    print("YES")
else:
    print("NO")