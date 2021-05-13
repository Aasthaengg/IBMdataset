def resolve():
  S_base = list(input())
  T = list(input())

  if len(T) > len(S_base):
    print("UNRESTORABLE")
    return True

  for i in reversed(range(len(S_base) - len(T) + 1)):
    isMatched = True
    for t in range(len(T)):
      if not (S_base[i + t] == T[t] or S_base[i + t] == "?"):
        isMatched = False
        break
    if isMatched:
      result = "".join(S_base[:i])+"".join(T)+"".join(S_base[i+len(T):])
      print(result.replace("?", "a"))
      return True

  print("UNRESTORABLE")

if __name__ == "__main__":
  resolve()