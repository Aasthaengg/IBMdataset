H1,M1,H2,M2,K = map(int,input().split())
timeW = M1 + H1 * 60
timeS = M2 + H2 * 60
print(timeS - timeW - K)