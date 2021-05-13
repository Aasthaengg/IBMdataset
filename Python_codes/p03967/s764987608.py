import sys
readline = sys.stdin.readline

S = readline().rstrip()

# パーを出せるときは必ずパーを出すのが最善
# g p g pの順で出せばよい
# 相手の手が、
# i % 2 == 0のとき
# gであれば0、pであれば-1
# i % 2 == 1のとき
# gであれば+1、pであれば0

ans = 0
for i in range(len(S)):
  if i % 2 == 0:
    if S[i] == "p":
      ans -= 1
  elif i % 2 == 1:
    if S[i] == "g":
      ans += 1
      
print(ans)