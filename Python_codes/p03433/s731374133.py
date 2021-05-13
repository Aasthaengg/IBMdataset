n = int(input())
a = int(input())
mod500 = n//500
remain = n - mod500 * 500
if a>=remain:
  print('Yes')
else:
  print('No')
