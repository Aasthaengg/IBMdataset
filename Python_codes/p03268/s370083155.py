N, K = map(int, input().split())

if K%2 == 1:
  cand = N // K
  ans = cand\
      + cand * (cand-1) * 3\
      + cand * (cand-1) * (cand-2)
  print(int(ans))
else:
  cand_mod0 = N // K
  ans_mod0 = cand_mod0\
           + cand_mod0 * (cand_mod0-1) * 3\
           + cand_mod0 * (cand_mod0-1) * (cand_mod0-2)
  cand_modhalf = N // K if N % K < K / 2 else (N // K) + 1
  ans_modhalf = cand_modhalf\
           + cand_modhalf * (cand_modhalf-1) * 3\
           + cand_modhalf * (cand_modhalf-1) * (cand_modhalf-2)
  print(int(ans_mod0 + ans_modhalf))