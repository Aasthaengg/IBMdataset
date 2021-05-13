n = list(input())
s = 0
for a in n:
    s += int(a)

if len(n) >= 2:
    if int(n[0]) >= 2:
        print(max(s, (len(n)-1)*9+int(n[0])-1))
    else:
        print(max(s, (len(n)-1)*9))
else:
    print(int(n[0]))