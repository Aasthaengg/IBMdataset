s=int(input())

if s<1200:
  res='ABC'
elif 1200<=s<2800:
  res='ARC'
else:
  res='AGC'
print(res)