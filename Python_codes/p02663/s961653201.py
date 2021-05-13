h1,m1,h2,m2,K = map(int,input().split())

print(((abs(h1-h2)*60)-(m1-m2)) - K)