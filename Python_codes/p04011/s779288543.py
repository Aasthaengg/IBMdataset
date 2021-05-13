N,K,X,Y = (int(input()) for T in range(0,4))
print(min(N,K)*X+max(0,N-K)*Y)