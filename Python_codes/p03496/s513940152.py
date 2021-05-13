import sys
N = int(input())
a_ls = list(map(int, input().split()))

Maxabs = 0
indofmaxabs = -1
for i in range(N):
    if Maxabs < abs(a_ls[i]):
        Maxabs = abs(a_ls[i])
        indofmaxabs = i
if Maxabs == 0:
    print(0)
    sys.exit()

print(2*(N-1))
# 符号を統一
for i in range(N):
    if not i == indofmaxabs:
        print(indofmaxabs+1,i+1)

# 階段にする
if a_ls[indofmaxabs] >= 0:
    for i in range(N-1):
        print(i+1,i+2)
else:
    for i in range(N-1,0,-1):
        print(i+1,i)

