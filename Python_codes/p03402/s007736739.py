a,b=map(int,input().split())

res = []
if a>10:
    while a>50:
        res.append("#."*50)
        res.append("#"*100)
        a -= 50
    while a>10:
        res.append("#."*10+ "#"*80)
        res.append("#"*100)
        a -= 10
    b -= 1
res.append("."*100)
while b > 50:
    res.append("#."*50)
    res.append("."*100)
    b-= 50
while b > 10:
    res.append("#."*10+ "."*80)
    res.append("."*100)
    b-= 10

if b>a:
    sa = b-a
    res.append("#."*sa+".."*(50-sa))
    res.append("."*100)
    for _ in range(a):
        res.append("#"*100)
        res.append("."*100)
    res.pop()
elif a>b:
    if b == 0:
        res.pop()
    res.append("#"*100)
    sa = a-b
    res.append(".#"*sa+"##"*(50-sa))
    res.append("#"*100)
    b -= 1
    for _ in range(b):
        res.append("."*100)
        res.append("#"*100)

else:
    for _ in range(a):
        res.append("#"*100)
        res.append("."*100)
    res.pop()

print(str(len(res))+" 100")
print("\n".join(res))