O = input()
E = input()
x = len(E)
ans = ""
for i in range(len(O)-1):
    ans += O[i]
    ans += E[i]

ans += O[len(O)-1]
try:
    ans += E[len(O)-1]
except IndexError:
    pass
print(ans)
