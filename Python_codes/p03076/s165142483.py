l,s = [],0
for _ in range(5):
    l.append(int(input()))
if len(set(l))==1:
    if l[0]%10 != 0:
        s = (10-(l[0]%10))*4
    print(sum(l) + s)
else:
    a = list(i%10 for i in l)
    b = list(10-i if i%10 else 0 for i in a)
    p = b.index(max(b))
    ans = 0
    for i in range(5):
        if l[i] != l[p]:
            ans += l[i]
            ans += b[i]
    print(ans+l[p])