def main():
  N, K = map(int, input().split())
  ans = 0
  for b in range(K+1, N+1):
    ans += ((N+1)//b*(b-K)+max(0, (N+1)%b-K))
    #print(b, ans)
  if K == 0:
    ans -= (N-K)
  print(ans)
if __name__ == "__main__":
  main()