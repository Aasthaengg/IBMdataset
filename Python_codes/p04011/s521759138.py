N,K,X,Y=int(input()),int(input()),int(input()),int(input())
print(K*X+(N-K)*Y if N > K else N*X)