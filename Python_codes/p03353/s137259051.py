s = input()
k = int(input())
d = set()
for n in range(1, 6):
    for i in range(len(s)):
        if i+n <= len(s):
            d.add(s[i:i+n])
sd = sorted(d)
print(sd[k-1])