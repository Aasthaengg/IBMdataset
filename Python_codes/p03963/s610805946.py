#ABC046.B
N,K = map(int,input().split())
if N >=2:
    c = K*(K-1)**(N-1)
elif N ==1 :
    c = K
print(c)