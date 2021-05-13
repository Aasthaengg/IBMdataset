s = input()
k = int(input())
a = []
for i in range(len(s)+1):
    for j in range(len(s)+1):
        if j <= k:
            a.append(s[i:i + j])
# print(a)
c = sorted(set(a))
# print(c)
print(c[k])