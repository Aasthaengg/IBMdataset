S = input()
if "C" in S and "F" in S:
  if S.index("C")<[i for i, x in enumerate(S) if x == "F"][-1]:
    print("Yes")
    exit()
print("No")
