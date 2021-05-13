O = input()
E = input()

ans = str()

for o,e in zip(O,E):
    ans += o + e
if len(O) == len(E):
    print(ans)
else:
    print(ans + O[-1])