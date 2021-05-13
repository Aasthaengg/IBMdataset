K,A,B=map(int,input().split())

if B-A<=2:
  print(K+1)
else:
  need_init=A-1
  if need_init>=K:
    print(K+1)
  else:
    K-=need_init
    answer=A
    
    answer+=(B-A)*(K//2)
    if K%2==0:
      print(answer)
    else:
      print(answer+1)