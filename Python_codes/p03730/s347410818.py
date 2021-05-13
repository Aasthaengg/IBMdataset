A, B, C = map(int, input().split())
aa = []
now = A
T = True
while T:
  if now % B == C:
    print("YES")
    T = False
    quit()
  else:
    if (now % B) not in aa:
      aa.append(now % B)
      now += A
      #print(aa)
    else:
      print("NO")
      quit()