n=int(input())
s=[input() for i in range(n)]
lastA=0
firstB=0
lastAandfirstB=0
ABs=0
for si in s:
    ABs+=si.count("AB")
    firstB+=(si[0]=="B")
    lastA+=(si[-1]=="A")
    lastAandfirstB+=(si[0]=="B")*(si[-1]=="A")

can=min(firstB,lastA)
# print(lastA,firstB,lastAandfirstB)
# if lastAandfirstB==1 and firstB==1 and lastA==1:
#     print(ABs)
#     exit()
if can==n or lastAandfirstB==firstB==lastA!=0:
    can=can-1
print(can+ABs)