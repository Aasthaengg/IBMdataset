S = input()

ans = 0
if S == "RSS" or S == "RSR" or S == "SRS" or S == "SSR":
  ans = 1
if S == "RRS" or S == "SRR":
  ans = 2
if S == "RRR":
  ans = 3

print(ans)
