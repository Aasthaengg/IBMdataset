o = input()
e = input()

ans = ''
for a, b in zip(list(o), list(e)):
    ans += a+b

if len(o)-len(e) > 0:
    ans += o[-1]
print(ans)