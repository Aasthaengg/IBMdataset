[N,M] = list(map(int,input().split()))
T = M*1900 + 100*(N-M)  #1かいの提出にかかる時間
print(T*2**M)