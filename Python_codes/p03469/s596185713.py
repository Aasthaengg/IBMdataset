S = input()
S_list = list(S)
S_list[S.index("7")] = "8"
a = ""
for i in S_list:
  a += i
print(a)