H, W = map(int, input().split())
S = [0]*(H+2)
S[0] = '#'*(W+2)
S[H+1] = '#'*(W+2)
for h in range(1,H+1):
  S[h] = '#' + input() + '#'
print(*S,sep='\n')