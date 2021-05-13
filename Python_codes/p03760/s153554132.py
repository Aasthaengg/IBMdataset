s1=list(input())
s2=list(input())

if len(s1)>len(s2):
    s2+=" "

s=[s1,s2]
sT=[list(x) for x in zip(*s)]

for i in range(len(s1)):
    print(sT[i][0],end="")
    print(sT[i][1],end="")
