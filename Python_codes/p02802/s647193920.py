N,M = map(int,input().split())
PS = [list(input().split()) for i in range(M)]

resultdict = {}
count_ans,count_pena = 0,0

for sub in PS :
    resultdict.setdefault(sub[0],{"AC":0, "WA":0})
    if resultdict[sub[0]]["AC"] == 0 :
        resultdict[sub[0]][sub[1]] += 1

for v in resultdict.values() :
    count_ans += v["AC"]
    if v["AC"] == 1 :
        count_pena += v["WA"]

print(count_ans,count_pena)