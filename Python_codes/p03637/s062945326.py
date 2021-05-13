N = int(input())
A=list(map(int,input().split()))
odd_num=0
bai_four=0
for i in range(N):
    if A[i]%2==1:
        odd_num=odd_num+1
    elif A[i]%4==0:
        bai_four=bai_four+1
if N%2==0:
    if odd_num <= bai_four:
        print('Yes')
    else:
        print('No')
else:
    if odd_num <= bai_four+1:
        print('Yes')
    else:
        print('No')