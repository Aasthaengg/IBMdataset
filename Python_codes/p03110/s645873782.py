N = int(input())
su = 0
for i in range(N):
  s = input()
  x = float(s[:-4])
  if s[-3:] == "JPY":
    su += x
  else:
    su += x*380000
    
print(su)