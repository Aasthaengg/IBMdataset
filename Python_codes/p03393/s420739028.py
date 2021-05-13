s = list(input())
l = [chr(i) for i in range(ord("a"), ord("z") + 1)]
if len(s) == 26:
    for i in range(26)[-2::-1]:
        for j in range(25, i, -1):
            if s[i] < s[j]:
                s[i] = s[j]
                print("".join(s[:i+1]))
                exit()
    print(-1)
    exit()
for i in range(26)[-1::-1]:
    if l[i] in s:
        del l[i]
s.append(l[0])
print("".join(s))