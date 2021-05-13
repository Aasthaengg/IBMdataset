N,K=list(map(int,input(' ').split(' ')))
print(min(N%K,(-N)%K))