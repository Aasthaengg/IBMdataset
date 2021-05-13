n = input()
N = list(n)
m = int(n)
if len(N) <= 2:
  if m >= 10:
    print(9)
  else:
    print(m)
    
elif 3 <= len(N) <= 4:
  if m >= 1000:
    print(9 + 900)
  else:
    print(9+m-99)
elif 5 <= len(N) <= 6:
  if m >= 100000:
    print(9 + 900 + 90000)
  else:
    print(9+ 900 + m - 9999)