s = input()
n = len(s)
res = False
for i in range(n):
    for j in range(i, n):
        if s[i] == 'C' and s[j] == 'F':
            res = True
if res: print("Yes")
else:   print("No")