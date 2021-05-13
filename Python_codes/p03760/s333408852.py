o = input()
e = input()
ans = ""
for n1, n2 in zip(o,e) :
    ans += n1
    ans += n2
if len(o) != len(e) :
    ans += o[len(o)-1]
print(ans)
