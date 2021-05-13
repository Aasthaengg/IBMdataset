r=int(input())
if r<1200:
  contest="ABC"
elif r<2800:
  contest="ARC"
else:
  contest="AGC"
print(contest)