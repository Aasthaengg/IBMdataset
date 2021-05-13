def f(x):
  if x == "A" or x == "C" or x == "G" or x == "T":
    return "1"
  else:
    return "0"
S = input()
s = list(S)
n = len(s)
u = list(map(f,s))
U = "".join(u)
print(max(list(map(len,U.split("0")))))

