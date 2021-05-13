s = input()
n = len(s)
s += "???"

i = 0
ans = 0

while i < n:
    abc = []
    if s[i] == "A":
        i += 1
        abc.append(0)
        while True:
            if s[i] == "A":
                i += 1
                abc.append(0)
            elif s[i:i+2] == "BC":
                i += 2
                ans += len(abc)
            else:
                break
    i += 1

print(ans)