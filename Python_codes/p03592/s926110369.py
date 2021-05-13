N,M,K=map(int,input().split())

if K% N==0 or K%M==0:
    print('Yes')
else:
    answers=[]
    for n in range(1,N+1):
        for m in range(1,M+1):
            answer=0
            answer+=n*M+m*N-n*m*2
            answers.append(answer)
    for n in range(1,M+1):
        for m in range(1,N+1):
            answer=0
            answer+=n*N+m*M-n*m*2
            answers.append(answer)
    if K in answers:
        print('Yes')
    else:
        print('No')
