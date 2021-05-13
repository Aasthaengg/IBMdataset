a,b,c = map(int,input().split())
ls = []
p = a%b
for i in range(1,b+2):
    q = p * i
    if q >= b:
        q %= b
    if q not in ls:
        ls.append(q)
    else:
        break
if c in ls:
    print("YES")
else:
    print("NO")