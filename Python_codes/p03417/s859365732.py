N,M=map(int,input().split())
print((-1 if N==1 else 1) * (N-2 if M==1 else (N-2)*(M-2)))
