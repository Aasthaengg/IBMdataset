N,A,B = map(int,input().split())
step = 0
if (B-A)%2 == 0:
    step = (B-A)//2
    print(step)
else:
    step = min(A,N-B+1)+(B-A-1)//2
    print(step)