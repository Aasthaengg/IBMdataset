N = int(input())
table = list(map(int,input().split()))

swap_count = 0

for i in range(0,len(table)-1): #最小値を持ってくる場所のループ
    for k in range(len(table)-1,i,-1):
        if table[k-1] > table[k]:
            table[k-1],table[k] = table[k],table[k-1]
            swap_count += 1

print(' '.join(map(str,table)))
print("%d"%(swap_count))

