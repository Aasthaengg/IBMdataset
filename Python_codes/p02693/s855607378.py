#A
K=int(input())
A, B=map(int,input().split())
Ans_list=[]
for i in range(A,B+1):
    if i%K==0:
        Ans_list.append(i)
if len(Ans_list)>0:
    print('OK')
else:
    print('NG')
