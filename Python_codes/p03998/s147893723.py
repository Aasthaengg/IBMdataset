a = input()
b = input()
c = input()
sa = []
sb = []
sc = []
for i in a:
    sa.append(i)
for i in b:
    sb.append(i)
for i in c:
    sc.append(i)
cur = sa.pop(0)
ans = ""
while True:
    if cur=="a":
        if not sa:
            ans = "A"
            break
        cur = sa.pop(0)
    if cur=="b":
        if not sb:
            ans = "B"
            break
        cur = sb.pop(0)
    if cur=="c":
        if not sc:
            ans = "C"
            break
        cur = sc.pop(0)
print(ans)