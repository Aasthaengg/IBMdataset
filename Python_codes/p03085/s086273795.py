dict_1 = {"A":"T","G":"C"}
dict_2 = {"T":"A","C":"G"}

s = input()
if s in dict_1:
  ans = dict_1[s]
else:
  ans = dict_2[s]

print(ans)