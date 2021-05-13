residence=[[[0 for i in range(10)] for j in range(3)] for k in range(4)]
n=int(input())
lines=[input() for i in range(n)]
for l in lines:
    k=list(map(int,l.split()))
    residence[k[0]-1][k[1]-1][k[2]-1]+=k[3]
    if residence[k[0]-1][k[1]-1][k[2]-1]>9: residence[k[0]-1][k[1]-1][k[2]-1]=9

for b in range(4):
    for f in range(3):
        print(' '+' '.join(map(str,residence[b][f])))
    if b!=3: print('#'*20)