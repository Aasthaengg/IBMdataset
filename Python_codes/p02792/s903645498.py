#import numpy as np

N = int(input())

l = [ [ 0 for i in range(9) ] for j in range(9) ]
#l = np.zeros((9,9), dtype=np.int)
# l[i][j] : i = 頭文字　j = 最後の文字

for k in range(N):
    x = str(k+1)
    i = int(x[0])
    j = int(x[-1])

    #print(i,j)

    if i == 0 or j == 0:
        continue
    l[i-1][j-1] += 1

ans = 0
for i in range(9):
    for j in range(i,9):
        if i == j:
            n = l[i][j]
            ans += n**2
        else:
            ans += l[i][j] * l[j][i] * 2
            

print(ans)







