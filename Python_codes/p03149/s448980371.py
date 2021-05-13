import itertools
X,Y,Z,N=input().split()
hako=[]
hako.append(X)
hako.append(Y)
hako.append(Z)
hako.append(N)
ans = ["1","9","7","4"]
kari=[]
for v in itertools.permutations(hako,4):
    kari.append(list(v))

if ans in kari:
    print("YES")
else:
    print("NO")