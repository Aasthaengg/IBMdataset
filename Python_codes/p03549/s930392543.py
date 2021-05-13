N, M = map(int, input().split())

print(int(((N-M)*100+1900*M)/(1/2)**M))