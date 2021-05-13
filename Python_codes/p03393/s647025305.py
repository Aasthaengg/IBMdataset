# 写経#2284578
S = input()
alp = "abcdefghijklmnopqrstuvwxyz"
def h(string, least = 'Z'):
  for c in alp:
    if c not in string:
      if c <= least:
        continue
      return string + c
  if string == "":
    return "-1"
  return h(string[:-1], string[-1])
print(h(S))