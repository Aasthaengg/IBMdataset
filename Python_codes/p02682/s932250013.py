A,B,C,K = list(map(int,input().split()))
print(max(min(K,A),0) - max(min(K-(A+B),C),0))