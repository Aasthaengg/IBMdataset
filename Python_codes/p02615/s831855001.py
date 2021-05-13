N = int(input())
A = sorted(map(int,input().split()),reverse = True)
answer = 0
i = 1
s = 0
answer = A[0]
if N == 2:
    anwer=A[0]
else:
    while True:
        s = (i+1)//2
        answer += A[s]
        i += 1
        if i == N-1:
            break
    
print(answer)