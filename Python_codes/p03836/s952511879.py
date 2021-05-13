A,B,C,D = map(int,input().split())
XX = C - A
YY = D - B
if XX >= 0:
  ans1 = 'R'*XX
  ans11 = 'L'*XX
elif XX < 0:
  ans1 = 'L'*abs(XX)
  ans11 = 'R'*abs(XX)
if YY >= 0:
  ans2 = 'U'*YY
  ans22 = 'D'*YY
elif YY < 0:
  ans2 = 'D'*abs(YY)
  ans22 = 'U'*abs(YY)
ans3 = ans1 + ans2
ans4 = ans11 + ans22

if XX >= 0 and YY >= 0:
  ans5 = 'L'+ ans2 +'U' +'R' + ans1 +'D'
  ans55 = 'R' + ans22 + 'D' + 'L' + ans11 + 'U'
elif XX < 0 and YY >= 0:
  ans5 = 'R' + ans2 + 'U' + 'L' + ans1 + 'D'
  ans55 = 'L' + ans22 + 'D' + 'R' + ans11 + 'U'
elif XX >=0 and YY <0:
  ans5 = 'L' + ans2 + 'D' + 'R' + ans1 +'U'
  ans55 = 'R' + ans22 + 'U' + 'L' + ans11 + 'D'
else:
  ans5 = 'R' + ans2 +'D' + 'L' + ans1 + 'U'
  ans55 = 'L' + ans22 + 'U' + 'R' + ans11 + 'D'
print(ans3+ans4+ans5+ans55)