N, K = map(int,input().split())
dices = list(map(int,input().split()))
list =[]
check=0
for i in range(K):
    check+=dices[i]
list.append(check)
for j in range(N-K):
    check -= dices[j]
    check += dices[j+K]
    list.append(check)    
print((max(list)+K)/2)