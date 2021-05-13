r,c = map(int, input().split())
I = []
for i in range(r):
    row = list(map(int, input().split()))
    I.append(row)

for i in range(r):
    s = sum(I[i])
    I[i].append(s)

new_i=[]
for j in range(c+1):
    s=0
    for i in range(r):
        s += I[i][j]
    new_i.append(s)
I.append(new_i)

for i in I:
    i = map(str, i)
    print(" ".join(i))