H1,M1,H2,M2,K=map(int,input().split())
T1 = H1 * 60 + M1
T2 = H2 * 60 + M2
if T2 < T1:
  T2 = T2 + 24 * 60
print(T2-T1-K)