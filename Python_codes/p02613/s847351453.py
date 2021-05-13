N = int(input())
cnt1 = 0
cnt2 = 0
cnt3 = 0
cnt4 = 0
for i in range(N):
  S = input()
  if S == 'AC':
    cnt1 += 1
  elif S == 'WA':
    cnt2 += 1
  elif S == 'TLE':
    cnt3 += 1
  else:
    cnt4 += 1
print( 'AC x ' + str(cnt1) )
print( 'WA x ' + str(cnt2) )
print( 'TLE x ' + str(cnt3) )
print( 'RE x ' + str(cnt4) )