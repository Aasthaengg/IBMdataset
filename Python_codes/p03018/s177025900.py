import sys
readline = sys.stdin.readline

S = readline().rstrip()
S = S.replace("BC","X")
S = S.replace("B",".").replace("C",".")
arr = S.split(".")
ans = 0
for a in arr:
  cnt = 0
  for i in range(len(a)):
    if a[i] == "X":
      ans += (i - cnt)
      cnt += 1
  
print(ans)