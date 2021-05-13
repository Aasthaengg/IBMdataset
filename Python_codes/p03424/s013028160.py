n = int(input())
arr = list(map(str, input().split()))
arr = list(set(arr))
if len(arr) == 3:
  print('Three')
elif len(arr) == 4:
  print('Four')