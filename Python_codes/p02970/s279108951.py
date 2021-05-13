N,D = map(int,input().split())

if N % (D*2+1)== 0:
    print(int(N / (D*2+1)))
else:
    print(int(N / (D*2+1)) + 1)