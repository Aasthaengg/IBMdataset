def main():
  S = list(input())
  T = list(input())
  
  if len(S) < len(T):
    print("UNRESTORABLE")
    return 0

  restorable = False
  LT = len(T)
  LS = len(S)
  for i in range(LS - LT + 1):
    if check_char(S[LS - LT - i : LS - i], T):
      restorable = True
      for j in range(LT):
        S[LS - LT - i + j] = T[j]
      break
  print("".join(["a" if s == "?" else s for s in S])) if restorable else print("UNRESTORABLE")

def check_char(A, B): # same length
  for i in range(len(B)):
    if A[i] not in [B[i], "?"]:
      return False
  return True

main()