s = input()
l = len(s)
for i in range(l):
    val = (l-i-1)
    if not val%2:
        sol = s[:val]
        if sol[:val//2]==sol[val//2:]:
            print(val);    break