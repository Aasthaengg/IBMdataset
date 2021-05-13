S = input()
K = int(input())

if len(set(S))==1:
  ans = int(len(S)*K/2)
elif K == 1:
  ans = 0
  serial = 1
  #print(serial)
  for i in range(len(S)-1):
    if S[i] == S[i+1]:
      serial += 1
    else:
      ans += int(serial/2)
      serial = 1
  ans += int(serial/2)
else:
  #first
  first=0
  serial = 1
  for i in range(len(S)-1):
    if S[i] == S[i+1]:
      serial += 1
    else:
      first += int(serial/2)
      serial = 1
  initial = 1
  for i in range(len(S)-1,1,-1):
    if S[i]==S[i-1]:
      initial += 1
    else:
      break
  cnt = 0
  serial = initial
  #print(serial)
  for i in range(len(S)):
    if S[i] == S[i-1]:
      serial += 1
    else:
      cnt += int(serial/2)
      serial = 1
    #print(cnt)
  #last
      
  #print(cnt)
  last = 0
  serial = initial
  for i in range(len(S)):
    if S[i] == S[i-1]:
      serial += 1
    else:
      last += int(serial/2)
      serial = 1
  last += int(serial/2)
  #print(first,cnt,last)
  ans = first+(K-2)*cnt+last

print(ans)