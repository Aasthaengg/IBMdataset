from scipy.special import comb

N,M=map(int,input().split())
base=0
base += comb(N, 2, exact=True)
base += comb(M, 2, exact=True)
print(base) # 10