import numpy as np
# 複数個格納
# A B = map(int, input().split())
# 行列化
# A = np.array(A)
# A=A.reshape(1,-1)
# A=A.T
#行列の比較
#C=((A%2 == vector0).all())


A = int(input())
B = int(input())
C = int(input())
X = int(input())

gohyaku=(np.arange(0,500*A+1,500)).reshape(1,-1)
hyaku=(np.arange(0,100*B+1,100)).reshape(1,-1)
goju=(np.arange(0,50*C+1,50)).reshape(1,-1)


gohyaku1=X-(gohyaku+hyaku.T)
count=0
for i in range(A+1):
    for k in range(B+1):
        if 0 <= gohyaku1[k,i] <= C*50:
            count=count+1

print(count)

