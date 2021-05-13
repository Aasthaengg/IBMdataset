from sys import stdin
input = stdin.readline


def main():
  S = input()[:-1]
  pre = 'R'
  r_cnt = 1
  l_cnt = 0
  l_pre = -1
  C = [0]*(len(S))
  for i in range(1, len(S)):
    now = S[i]
    if pre == 'R' and now == 'R':
      r_cnt += 1
    elif pre == 'R' and now == 'L':
      C[i-1] = r_cnt
      r_cnt = 0
      l_pre = i
      l_cnt = 1
    elif pre == 'L' and now == 'L':
      l_cnt += 1

    if (pre == 'L' and now == 'R') or (i == len(S)-1):
      C[l_pre] = l_cnt
      l_cnt = 0
      r_cnt = 1
      ave = int((C[l_pre] + C[l_pre-1]) / 2)
      if (C[l_pre] + C[l_pre-1]) % 2 == 0:
        C[l_pre-1], C[l_pre] = ave, ave
      else:
        n_move = max(C[l_pre-1], C[l_pre]) - 1
        if n_move % 2 == 0:
          if C[l_pre-1] > C[l_pre]:
            C[l_pre-1], C[l_pre] = ave+1, ave
          else:
            C[l_pre-1], C[l_pre] = ave, ave+1
        else:
          if C[l_pre-1] > C[l_pre]:
            C[l_pre-1], C[l_pre] = ave, ave+1
          else:
            C[l_pre-1], C[l_pre] = ave+1, ave

    pre = now

  print(*C, sep=' ')


if(__name__ == '__main__'):
  main()
