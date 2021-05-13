N=int(input())
S=list(input())
a1=[i for i in range(0,(N//2))]
a2=[i for i in range((N//2),N)]
a3=[S[i] for i in a1]
a4=[S[i] for i in a2]
print('Yes' if a3==a4 else 'No')