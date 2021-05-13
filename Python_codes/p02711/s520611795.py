N = int(input())
ans = "No"
if N % 10 == 7:
  ans = "Yes"
if ( N // 10 ) % 10 == 7:
  ans = "Yes"
if ( N // 100 ) % 10 == 7:
  ans = "Yes"
print(ans)