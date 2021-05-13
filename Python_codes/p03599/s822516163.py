a, b, c, d, e, f = map(int, input().split())
sug, dif2 = 0, 100
s = {}
wat1, wat2 = 100*a, 100*b
cap1, cap2 = a*e, b*e
for i in range(1,f//wat1+1):
    for j in range(f//wat2+1):
        if (wat1+cap1)*i+(wat2+cap2)*j<=f:
            s[cap1*i+cap2*j] = wat1*i+wat2*j
if s == {}:
    dif1 = f-wat1
    for i in range(10):
        for j in range(10):
            if 0<=(f-wat1)-(c*i+d*j)<dif1:
                dif1 = (f-wat1)-(c*i+d*j)
                sug3 = c*i+d*j
    print(wat1+sug3, sug3)
    exit(0)
for i in s.keys():
    for j in range(i//c+1):
        for k in range(i//d+1):
            if 0<=i-(c*j+d*k)<dif2:
                dif2 = i-(c*j+d*k)
                wat,sug1,sug2 = s[i],j,k
print(c*sug1+d*sug2+wat, c*sug1+d*sug2)
