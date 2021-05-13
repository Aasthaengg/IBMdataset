K=int(input())
nana=[7]
for i in range(0,K):
    if nana[i]%K==0:
        print(i+1)
        break
    nana.append((nana[i]*10+7)%K)
    if i==K-1:
        print("-1")
        break