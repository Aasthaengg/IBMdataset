H1,M1,H2,M2,K = map(int,input().split())
A = (H1 * 60) + M1
B = (H2 * 60) + M2
C = B - A
print(C-K)