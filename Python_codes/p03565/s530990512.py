#!/usr/bin/env python3

# input = stdin.readline

def solve(s,t):
  s_len = len(s)
  t_len = len(t)
  k = 0
  l = []
  while k + t_len <= s_len:
    flag = True
    for i in range(t_len):
      if s[k+i] == t[i] or s[k+i] == "?":
        pass
      else:
        flag = False
    cand = "".join((s[:k],t,s[k+t_len:])).replace("?","a")
    if flag:
      l.append(cand)
    k += 1
  if len(l) == 0:
    return "UNRESTORABLE"
  else:
    return list(sorted(l))[0]


def main():
  s = input()
  t = input()
  print(solve(s,t))
  return

if __name__ == '__main__':
  main()
