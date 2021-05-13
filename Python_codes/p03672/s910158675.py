S = input().strip()
N = len(S)
for i in range(1,N-1):
    if (N-i)%2==0 and S[:(N-i)//2]==S[(N-i)//2:N-i]:
        print(N-i)
        break