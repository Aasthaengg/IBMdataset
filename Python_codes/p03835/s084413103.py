K,S = map(int,input().split())
num = 0
for i in range(K+1):
    for j in range(K+1):
        if i + j <= S and K + i + j >= S:
            num += 1
print(num)