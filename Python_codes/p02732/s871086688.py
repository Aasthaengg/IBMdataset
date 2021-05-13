
N = int(input())
A = list(map(int,input().split()))
# print('A:',A)
#まず、一気に数えてしまおう！
num = [0]*N
for i in range(N):
    num[A[i]-1]+=1
# print('num:',num)


#その数のペアはいくつ？
C = [0]*N
cnt=0 #１つも抜かさない時の選び出す場合の数

for i in range(N):
    if num[i]!=0 and num[i]!=1:
        dammy = (num[i] * (num[i]-1))//2
        cnt+=dammy
        C[i] = dammy
# print('cnt,C:',cnt,C)


#実際に計算していく
for i in range(N):
    # print('A[i]',A[i])
    print(cnt - C[A[i]-1] + ((num[A[i]-1]-1)*(num[A[i]-1]-2)) //2)
        # print('ue')
