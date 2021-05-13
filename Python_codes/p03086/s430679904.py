S = input()
check = set("AGCT")

max_cnt = 0
for i in range(len(S)):
  cnt = 0
  for j in range(0,len(S)-i):
    #print(S[i+j],end="")
    if S[i+j] in check:
      cnt += 1
      max_cnt = max(max_cnt,cnt)
    else:
      break
      
print(max_cnt)
