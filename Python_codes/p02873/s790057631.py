s = input()
n = len(s)
a = [0]
for i in range(n):
    if s[i] == ">":
        temp = a[-1] - 1
        a.append(temp)
        if i == n - 1 or s[i + 1] == "<":
            a[i + 1] = 0
            for j in range(i, -1, -1):
                if s[j] == ">":
                    if s[j - 1] == "<":
                        a[j] = max(a[j], a[j + 1] + 1)
                    else:
                        a[j] = a[j + 1] + 1
                else:
                    break
    else:
        a.append(a[-1] + 1)
print(sum(a))