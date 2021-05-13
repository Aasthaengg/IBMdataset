N,K = map(int,input().split())
x = (N+1)//2
bl = (x >= K)
answer = 'YES' if bl else 'NO'
print(answer)