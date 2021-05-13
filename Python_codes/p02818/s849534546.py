def main():
  a,b,k= list(map(int,input().split()))
  if a >= k :
    print(a-k,b)
  elif a+b >= k:
    print(0,b-(k-a))
  else:
    print(0,0)

main()