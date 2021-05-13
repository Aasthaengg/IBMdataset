N=int(input())
S=input()

MAX=0
for i in range(1,N-1):
  s1,s2=set(S[:i]),set(S[i:])
  tmp = len(s1.intersection(s2))
  if tmp > MAX:MAX=tmp

print(MAX)