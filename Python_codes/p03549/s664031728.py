def judge(N,M):
  return 2**M*(1900*M+100*(N-M))

N,M = map(int,input().split())
print(judge(N,M))