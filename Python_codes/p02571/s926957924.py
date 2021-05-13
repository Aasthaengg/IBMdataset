match_cnt = 0

S = input()
T = input()

S_len = len(S)
T_len = len(T)

for S_idx in range(S_len - T_len + 1):
  cnt = 0

  for T_idx in range(T_len):
    if(S[S_idx + T_idx] == T[T_idx]):
      cnt += 1
  
  if( cnt > match_cnt ):
    match_cnt = cnt

print(T_len - match_cnt)