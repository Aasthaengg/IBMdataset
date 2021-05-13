mod = 10**9 + 7
n = int(input())
caps = ['A','G','C','T']
agct = []
for a in caps:
    for b in caps:
        for c in caps:
            if a+b+c not in ['AGC','GAC','ACG']:
                agct.append(a+b+c)

ngs = set(['AGC','GAC','ACG','AGGC','ATGC','AAGC','AGAC','AGTC'])           
dic = {}
for trio in agct:
        dic[trio] =1
for _ in range(n-3):
    dic2 = {x:0 for x in agct}
    for trio in agct:
        for cap in caps:
            quad = trio + cap
            if (not quad in ngs) and (not quad[1:] in ngs):
                dic2[quad[1:]] += dic[trio]
    dic = dic2

print(sum(dic.values())%mod)