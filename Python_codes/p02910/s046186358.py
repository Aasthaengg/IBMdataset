import sys
S = input()
n = len(S)
for i in range(n):
  if ((i+1) % 2 != 0 and S[i] == 'L') or ((i+1) % 2 == 0 and S[i] == 'R'):
    print('No')
    sys.exit()
print('Yes')