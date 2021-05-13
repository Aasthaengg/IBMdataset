s = input()
p = list(map(int,s))

for x in range(2**3):
    ans = p[0]
    for y in range(3):
        if (x>>y)&1:
            ans += p[y+1]
        else:
            ans -= p[y+1]
    if ans == 7:
        kotae = format(x,"#05b")

kotae = kotae[2:]
for z in range(3):
    print(str(p[z]),end="")
    if kotae[-z-1] == str(1):
        print("+",end="")
    else:
        print("-",end="")

print(str(p[3]) + "=7" )
