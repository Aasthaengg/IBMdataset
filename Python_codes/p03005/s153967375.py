N,K=map(int,input().split())

if N > K and K !=1:
	wide = N - K
elif N == K or K==1:
  	wide = 0
else:
    wide = 0
    
print(wide)