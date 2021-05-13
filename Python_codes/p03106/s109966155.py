A, B, K = map(int,input().split())

C = min(A, B)

cnt = 0

while(1):
    if(A % C == 0 and B % C == 0):
        cnt+=1
    if(cnt == K):
        print(C)
        exit()
    C -= 1
