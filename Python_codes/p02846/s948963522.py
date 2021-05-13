t1, t2 = list(map(int, input().split()))
a1, a2 = list(map(int, input().split()))
b1, b2 = list(map(int, input().split()))

fin_gap = t1 * (a1 - b1) + t2 * (a2 - b2)
mid_gap = t1 * (a1 - b1) 

if fin_gap == 0:
  print("infinity")
else:
  if mid_gap * fin_gap > 0:
    print(0)
  else:
    
    mod = abs(mid_gap) % abs(fin_gap)
    q = abs(mid_gap) // abs(fin_gap)
    
    if mod == 0:
      ans = q * 2
    else:
      ans = q * 2 + 1
    
    print(ans)