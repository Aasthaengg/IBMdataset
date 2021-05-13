L = list(input())
N = int(input())
ANS = []
for i in range(len(L)) :
    if i % N == 0 :
        ANS.append(L[i])
ans = "".join(ANS)
print(ans)
