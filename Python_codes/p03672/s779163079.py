S=input()[:-1]

def is_even(seq):
  return seq[:len(seq)//2]==seq[len(seq)//2:]

for i in range(len(S)):
  s = S[:len(S)-i]
  if len(s)%2==0 and is_even(s):
    print(len(s))
    exit()