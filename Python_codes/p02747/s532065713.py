S = input()
count = 0
count_h = 0
count_i = 0
frag = 0
for i in range(len(S)-1):
  if S[i] == 'h' and S[i+1] == 'i':
    count = 1
for i in range(len(S)):
  if S[i] == 'h':
    count_h = count_h+1
  elif S[i] == 'i':
    count_i = count_i+1
i = 0
while i < len(S):
  if S[i] != 'h':
    frag = 1
  i = i+2

if count == 1 and len(S)%2 == 0 and count_h == count_i and frag == 0:
  print('Yes')
else:
  print('No')