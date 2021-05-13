N = int(input())
S = [input() for i in range(N)]
 
c0 = 0
c1 = 0
c2 = 0
c3 = 0
 
for i in range(N):
  if S[i] == 'AC':
    c0 += 1
  elif S[i] == 'WA':
    c1 += 1
  elif S[i] == 'TLE':
    c2 += 1
  elif S[i] == 'RE':
    c3 += 1
 
print('AC x %d' %c0)
print('WA x %d' %c1)
print('TLE x %d' %c2)
print('RE x %d' %c3)