from scipy.special import comb
a,b=map(int,input().split())
print(int(comb(a,2)+comb(b,2)))