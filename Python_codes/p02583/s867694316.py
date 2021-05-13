k = int(input())

an = input().split()

for i in range(len(an)):
    an[i] = int(an[i])

ln = sorted(an)

ans = 0

for i in range(k):
    for j in range(i,k):    
        for l in range(j,k):
            a1 = int(ln[i])
            a2 = int(ln[j])
            a3 = int(ln[l])
            if a1!=a2 and a2 != a3:
                m = a1 + a2
                if a3 < m:
                    ans += 1

print(ans)