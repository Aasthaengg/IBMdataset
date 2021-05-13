import sys
readline = sys.stdin.readline

X = readline().rstrip()

cnt = 0
ans = 0
# Sが出たら1増やし、Tが出たら1減らす
# 0のときにTが出たらansを+1する。ans * 2が答え
for i in range(len(X)):
  if X[i] == "S":
    cnt += 1
  else:
    if cnt == 0:
      ans += 1
    else:
      cnt -= 1
      
print(ans * 2)