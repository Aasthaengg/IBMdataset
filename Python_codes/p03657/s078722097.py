A, B = map(int, input().split())
ans = 'Impossible'
if A % 3 == 0:
  ans = 'Possible'
elif B % 3 == 0:
  ans = 'Possible'
elif (A+B) % 3 == 0:
  ans = 'Possible'
print(ans)