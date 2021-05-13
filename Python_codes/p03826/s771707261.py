A,B,C,D = map(int,input().split())
#print(A,B,C,D)

ans1 = A*B
ans2 = C*D

if ans1 == ans2:
  print(ans1)
elif ans1 > ans2:
  print(ans1)
else:
  print(ans2)