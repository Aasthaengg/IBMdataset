s = input()


start = []
finish = []

for i in range(len(s)):
    if s[i] == "A":
        start.append(i)
    elif s[i] == "Z":
        finish.append(i)
    else:
        pass

ans = finish[-1] - start[0] +1
print(ans)
