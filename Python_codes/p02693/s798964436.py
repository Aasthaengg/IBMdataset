K=int(input())
A,B=map(int,input().split())
AB_list = [i for i in range(A,B+1) if i % K == 0]
if len(AB_list) != 0:
    print('OK')
else:
    print('NG')
