s = input()
c = list(s)
c2 = set(c)
al = sorted(list("qwertyuiopasdfghjklzxcvbnm"))
#26文字未満なら追加

if len(c)<26:
    for i in range(26):
        if al[i] not in c2:
            print(s+al[i])
            exit()

if s == "zyxwvutsrqponmlkjihgfedcba":
    print(-1)
    exit()

rev = "zyxwvutsrqponmlkjihgfedcba"
for i in range(25,-1,-1):
    x = sorted(c[i:])
    for j in x:
        if ord(s[i])<ord(j):
            print(s[:i]+j)
            exit()