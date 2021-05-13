S = input()
T = input()
 
cnt = 0
for si, ti in zip(S, T):
  if si != ti:
    cnt += 1
    
print(cnt)