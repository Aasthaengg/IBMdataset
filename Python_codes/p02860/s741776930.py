N=int(input())
S=str(input())
if S[0:N//2]==S[N//2:N]:
    print('Yes')
else:
    print('No')