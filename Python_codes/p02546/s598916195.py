def func(S):
  if S[-1] == "s":
    return S+"es"
  else:
    return S+"s"


if __name__ == "__main__":
    S = input()
    print(func(S))