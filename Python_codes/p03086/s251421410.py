from sys import stdin

s = stdin.readline().strip()

def is_acgt(ss):
  sset = set(ss)
  sset.discard('A')
  sset.discard('G')
  sset.discard('C')
  sset.discard('T')
  return len(sset) == 0

for i in range(1, len(s)+1)[::-1]:
  for j in range(len(s) - i + 1):
    ss = s[j:j+i]
    if is_acgt(ss):
      print(i)
      exit()
      
print(0)