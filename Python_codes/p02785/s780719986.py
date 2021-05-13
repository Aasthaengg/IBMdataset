import math

def main():
  N, K = map(int, input().split())
  H = list(map(int, input().split()))
  
  if K >= N:
    print(0)
    return
  
  #ans = 0
  l = sorted(H, reverse=True)
  
  # del l[:K]
  # print(l)
  
  # ans += sum(l)
  
  print(sum(l[K:]))
  #print(ans)
  
  
main()