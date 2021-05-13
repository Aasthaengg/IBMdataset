s=input()
s = list(s)

n=int(input())
i = 0
res = []

while i < len(s):
    res.append(s[i])
    i += n

print(''.join(res))