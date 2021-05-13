s=input()

def ans(s):
  if "RRR" in  s:
    return 3
  elif "RR" in s:
    return 2
  elif "R" in s:
    return 1
  else:
    return 0
print(ans(s))