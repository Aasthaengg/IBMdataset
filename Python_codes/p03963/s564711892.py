N,M  = map(int,input().split(" "))
Ans = M
if N>1:
    for _ in range(N-1):
        Ans*=M-1
print(Ans)