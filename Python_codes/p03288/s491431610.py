N = int(input())

ans = ['ABC', 'ARC', 'AGC']

if N < 1200:
  print(ans[0])
elif N < 2800:
  print(ans[1])
else:
  print(ans[2])