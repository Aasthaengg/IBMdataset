o=input()
e=input()
print("".join([o[i]+e[i] for i in range(len(o)-1)]),end="")
print(o[-1],end="")
if len(o) == len(e):
  print(e[-1])