N,M,C=map(int,input().split())
B=input()
A=[input() for i in range(N)]

def ans121(N:int, M:int, C:int, B:str, A:list):
    B=list(map(int,B.split()))
    judge_count=0
    for i in range(N):
        A_list=list(map(int,A[i].split()))#N回検証を繰り返す
        math_count=0
        for j in range(M):#リストの中の要素Mの数だけB[j]*A_list[j]を繰り返し足していく
           math_count+=B[j]*A_list[j]
        if math_count+C>0:
           judge_count+=1
    return judge_count

print(ans121(N,M,C,B,A))
