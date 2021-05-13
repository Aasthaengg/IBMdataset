n = int(input())

citydic = {}
for i in range(n):
    s,p = map(str,input().split())
    if s not in citydic:
        citydic[s] = [[int(p),i+1]]
    else:
        citydic[s].append([int(p),i+1])
        citydic[s].sort(reverse=True)

citydic = sorted(citydic.items())

for k in citydic:
    for v in k[1:]:
        for n in v:
            print(n[1])