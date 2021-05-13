from sys import stdin
input = stdin.readline


def main():
  S = input()[:-1]
  T = input()[:-1]

  t_start_idx = []
  for si, s in enumerate(S):
    # print(f's:{s}')
    if not(s == T[0]) and not(s == '?'):
      continue
    cur_si = si
    for t in T:
      # print(f't:{t}')
      if cur_si >= len(S): break
      if not(t == S[cur_si]) and not(S[cur_si] == '?'):
        break
      cur_si += 1
    else:
      t_start_idx.append(si)
      continue

  if not len(t_start_idx):
    print('UNRESTORABLE')
    return

  new_S = S[:t_start_idx[-1]] + T + S[t_start_idx[-1]+len(T):]
  # print(new_S)

  ret_s = ''
  for s in new_S:
    if s == '?':
      ret_s += 'a'
    else:
      ret_s += s

  print(ret_s)


if(__name__ == '__main__'):
  main()