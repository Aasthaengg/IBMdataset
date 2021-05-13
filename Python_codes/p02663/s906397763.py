H1,M1,H2,M2,K = map(int, input().split())

TIME = (H2-H1)*60
TIME = TIME+(M2-M1)

print(TIME-K)