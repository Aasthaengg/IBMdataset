s = input()
n = len(s)

list = ["dream", "dreamer", "erase", "eraser"]

s = s[::-1]

while True:
    if s.startswith(list[0][::-1]):
        n -= 5
        s = s[5:]
    elif s.startswith(list[1][::-1]):
        n -= 7
        s = s[7:]
    elif s.startswith(list[2][::-1]):
        n -= 5
        s = s[5:]
    elif s.startswith(list[3][::-1]):
        n -= 6
        s = s[6:]
    else:
        break

if s == "":
    print("YES")
else:
    print("NO")