n = int(input())
s = input()
if len(s) > n:
  print(f'{s[:n]}...')
else:
  print(s)