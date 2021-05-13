S=input()
if S[0] != 'A':
  print('WA')
  exit()
count=0
for i in range(2,len(S)-1):
  if S[i]=='C':
    count+=1
if count != 1:
  print('WA')
  exit()

for i in range(1,len(S)):
  if S[i] != 'C' and (ord(S[i])<97 or ord(S[i])>122):
    print('WA')
    exit()

print('AC')