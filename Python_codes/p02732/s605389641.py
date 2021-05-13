def main():
  N=int(input())
  A=[int(a) for a in input().split()]
  cnt={}
  for a in A:
    cnt[a] = cnt.get(a, 0) + 1
  prob=0
  for a in cnt.values():
    prob+=a*(a-1)//2
    
  for a in A:
    print(prob-(cnt[a]-1))
  
main()

