
def main():
  N = int(input())
  S, T = input().split()
  ans = ''
  
  for i in range(0, N):
    ans += S[i] + T[i]
    
  print(ans)
  
  
main()