N,K = (int(input()) for T in range(0,2))
Num = 1
for TN in range(0,N):
    Num = min(2*Num,Num+K)
print(Num)