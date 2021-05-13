import fractions
def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)


n,m = map(int,input().split())

s1=input()

s2=input()

len_moji = lcm(n,m)

len_s1 = []

len_s2 = []

for i in range(n):
    len_s1.append(i*len_moji//n+1)

for i in range(m):
    len_s2.append(i*len_moji//m+1)
#print(len_s1)
#print(len_s2)
count = 0
for ix, vs1 in enumerate(len_s1):
    for jx in range(count,len(len_s2)):
        #print(vs1, len_s2[jx])
        if vs1 < len_s2[jx]:
            count = jx-1
            break
        if vs1 == len_s2[jx]:
            count = jx
            if s1[ix] != s2[jx]:
                print(-1)
                exit()
            break
print(len_moji)