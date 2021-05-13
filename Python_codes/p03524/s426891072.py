# submit#2
s = input().rstrip()
v = [0, 0, 0]
for i in range(len(s)):
    if s[i] == 'a':
        v[0] = v[0] + 1
    elif s[i] == 'b':
        v[1] = v[1] + 1
    elif s[i] == 'c':
        v[2] = v[2] + 1

result = 'NO'
kind = 0
for i in range(len(v)):
    if v[i] != 0:
        kind = kind + 1

if len(s) <= 3:
    if kind == len(s):
        result = 'YES'

else:
    if kind == 3:
        minv = min(v)
        for i in range(len(v)):
            v[i] = v[i] - minv

        if sum(v) < 3:
            kind = 0
            for i in range(len(v)):
                if v[i] != 0:
                    kind = kind + 1

                if kind == sum(v):
                    result = 'YES'

print(result)
