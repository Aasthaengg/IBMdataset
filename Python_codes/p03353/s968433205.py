s = input()
k = int(input())
a = set()
for i in range(len(s)+1):
    for j in range(i, min(i+6, len(s)+1)):
        a.add(s[i:j])
print(sorted(a)[k])
