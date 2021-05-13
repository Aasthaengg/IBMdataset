w=str(input())
W=list(set(list(w)))
for i in range(len(W)):
    if w.count(W[i])%2!=0:
        print('No')
        exit()
print('Yes')