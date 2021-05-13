inputs = [int(c) for c in input().split()]
ans = inputs[0] - inputs[1] if inputs[3] % 2 == 0 else inputs[1] - inputs[0]
if ans > 10**18:
  print("Unfair")
else:
  print(ans)
