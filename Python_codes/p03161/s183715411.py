def main():
  N,K=map(int,input().split())
  h=list(map(int,input().split()))
  DP=[0]*N
  for i in range(1,N):
    min_k=float('inf')
    min_k=min([DP[j]+abs(h[i]-h[j]) for j in range(max(i-K,0),i)])
    DP[i]=min_k
    pass
  print(DP[-1])

if __name__ == '__main__':
  main()

