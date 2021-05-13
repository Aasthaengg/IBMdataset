H1,M1,H2,M2,K = map(int,input().split())
h1 = 60*H1+M1
h2 = 60*H2+M2
d = h2-h1
print(d-K)