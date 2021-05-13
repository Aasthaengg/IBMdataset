x = input()
s = 0
ans = len(x)
for c in x:
    if c=='S':
        s += 1
    elif s>0:
        ans -= 2
        s -= 1
print(ans)