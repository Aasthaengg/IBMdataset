import itertools

s=dict()
for i in itertools.product(["A","C","G","T"], repeat=3):
    s[i]=1
s[("A","G","C")]=0
s[("G","A","C")]=0
s[("A","C","G")]=0

n=int(input())

mod=10**9+7
nn=3
t=dict()
while nn<n:
    for i in itertools.product(["A","C","G","T"], repeat=3):
        t[i]=0
    nn+=1
    for ky in s.keys():
        if ky[0]=="G" and ky[1]=="C":
            t[("A",ky[0],ky[1])]=0
            t[("C",ky[0],ky[1])]+=s[(ky[0],ky[1],ky[2])]
            t[("G",ky[0],ky[1])]+=s[(ky[0],ky[1],ky[2])]
            t[("T",ky[0],ky[1])]+=s[(ky[0],ky[1],ky[2])]
        elif ky[0]=="A" and ky[1]=="C":
            t[("A",ky[0],ky[1])]+=s[(ky[0],ky[1],ky[2])]
            t[("C",ky[0],ky[1])]+=s[(ky[0],ky[1],ky[2])]
            t[("G",ky[0],ky[1])]=0
            t[("T",ky[0],ky[1])]+=s[(ky[0],ky[1],ky[2])]
        elif ky[0]=="C" and ky[1]=="G":
            t[("A",ky[0],ky[1])]=0
            t[("C",ky[0],ky[1])]+=s[(ky[0],ky[1],ky[2])]
            t[("G",ky[0],ky[1])]+=s[(ky[0],ky[1],ky[2])]
            t[("T",ky[0],ky[1])]+=s[(ky[0],ky[1],ky[2])]
        elif ky[0]=="G" and ky[2]=="C":
            t[("C",ky[0],ky[1])]+=s[(ky[0],ky[1],ky[2])]
            t[("G",ky[0],ky[1])]+=s[(ky[0],ky[1],ky[2])]
            t[("T",ky[0],ky[1])]+=s[(ky[0],ky[1],ky[2])]
        elif ky[1]=="G" and ky[2]=="C":
            t[("C",ky[0],ky[1])]+=s[(ky[0],ky[1],ky[2])]
            t[("G",ky[0],ky[1])]+=s[(ky[0],ky[1],ky[2])]
            t[("T",ky[0],ky[1])]+=s[(ky[0],ky[1],ky[2])]
        else:
            t[("A",ky[0],ky[1])]+=s[(ky[0],ky[1],ky[2])]
            t[("C",ky[0],ky[1])]+=s[(ky[0],ky[1],ky[2])]
            t[("G",ky[0],ky[1])]+=s[(ky[0],ky[1],ky[2])]
            t[("T",ky[0],ky[1])]+=s[(ky[0],ky[1],ky[2])]
    for ky in s.keys():
        s[ky]=t[ky]           

icnt=0
for i in s.values():
    icnt=(icnt+i)%mod
print(icnt)

