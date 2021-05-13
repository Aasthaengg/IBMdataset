h,m,H,M,K = map(int, input().split()) 

d = H*60+M-(h*60+m)
print(d-K)