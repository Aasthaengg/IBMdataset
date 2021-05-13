s = input()
w = int(input())
a = []
i = 0
while i <= len(s)-1:
    a.append(s[i])
    i += w
print("".join(a))
