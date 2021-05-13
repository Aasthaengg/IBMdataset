N, M = map(int, input().split())

for i in range((M+1)// 2):
    print(1+i, (M+1)//2*2 - i)

for j in range(M//2):
    print((M+1)//2*2+1 + j, 2*M + 1 - j)