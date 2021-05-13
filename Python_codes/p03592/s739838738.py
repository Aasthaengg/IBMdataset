n, m, k = map(int,input().split())

for i in range(min(n,m)+1):
    for j in range(max(n,m)+1):
        tmp = max(n,m)*i + min(n,m)*j - 2*i*j
        if tmp == k:
            print('Yes')
            exit()
                
print('No')