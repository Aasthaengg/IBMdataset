# 初期入力
N= int(input())
S =input().strip()

# RGBの各index
R =set([i for i, x in enumerate(S) if x == 'R'])
G =set([i for i, x in enumerate(S) if x == 'G'])
B =set([i for i, x in enumerate(S) if x == 'B'])


count =0
rgb =[]
for i in R:
    for j in G:
        k1 =j +(j -i)
        if k1 in B: #inはlistよりsetのほうが速い
            count +=1

for i in B:
    for j in R:
        k1 =j +(j -i)
        if k1 in G: #inはlistよりsetのほうが速い
            count +=1

for i in G:
    for j in B:
        k1 =j +(j -i)
        if k1 in R: #inはlistよりsetのほうが速い
            count +=1

all =len(R) *len(G) *len(B)
print(all -count)