l, r=len, range
N= int(input())
c1= input().split()
c2=c1[:]
for i in r(l(c1)):
    for j in r(i+1, l(c1))[::-1]:
        if c1[j][1]< c1[j-1][1]:
            c1[j], c1[j-1]= c1[j-1], c1[j]

    m= i
    for j in r(i, l(c2)):
        if c2[j][1] < c2[m][1]: m= j
    c2[i], c2[m]= c2[m], c2[i]
print(*c1)
print("Stable")
print(*c2)
print("Stable" if c1==c2 else "Not stable")