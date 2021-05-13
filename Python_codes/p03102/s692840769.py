# B - Can you solve this?
#行列の入力方法を習得する 2020/08/07
N,M,C = map(int,input().split())
B = list(map(int,input().split()))

'''
A = []
for o in range(N):#文字列の行列を入力
    a = input().split()
    A.append(a)
print(A)

A_list = []
for p in range(N):
    box = []
    for q in range(M):
        aa = int(A[p][q])
        box.append(aa)
    A_list.append(box)
print(A_list)
'''
A_list = []#任意の列数の行列の入力
for o in range(N):
    A = list(map(int, input().split()))
    A_list.append(A)
    
count = 0
for i in  range(N):
    judge = C
    for j in range(M):
        judge += A_list[i][j]*B[j]
    if judge > 0:
        count += 1
print(count)