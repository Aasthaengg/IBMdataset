N, M = map(int, input().split())

loop = (2**M)
print(1900*loop*M+100*(N-M)*loop)
