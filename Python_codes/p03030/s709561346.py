n = int(input())
sp ={}
l = [] 
for i in range(n):
    s,p = input().split()
    sp ={}
    sp["index"] = i+1
    sp["name"] = s
    sp["score"] = int(p)
    l.append(sp)


for dic in sorted(l, key=lambda x: (x["name"], -x["score"])):
    print(dic["index"])