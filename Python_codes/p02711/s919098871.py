n = int(input())
ans = 'No'
if n % 10 == 7:
  ans = 'Yes'
elif (n // 10) % 10 == 7:
  ans = 'Yes'
elif (n // 100) % 10 == 7:
  ans = 'Yes'

print(ans)