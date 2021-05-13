n,m=map(int,input().split())

if m==0:
    print(0,0)
    import sys
    sys.exit()

p=[list(input().split()) for _ in range(m)]
correct=set([p[i][0] for i in range(m) if p[i][1]=='AC'])

s=set()
sum_wa=0

for i in [p[j] for j in range(m) if p[j][0] in correct]:
    if i[0] in s:
        continue
    else:
        if i[1]=='WA':
            sum_wa+=1
        else:
            s.add(i[0])

print(len(correct),sum_wa)