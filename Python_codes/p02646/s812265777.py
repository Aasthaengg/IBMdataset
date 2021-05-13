A, V = map(int, input().split(" "))
B, W = map(int, input().split(" "))
T = int(input())

if W > V:
  print("NO")
else:

  if abs(A - B) <= T * (V - W):
    print("YES")
  else:
    print("NO")

# if A - B > 0:
#   # 負の方向に逃げる
#   if (B + 10**9) / W <= T:
#     # print("left reach")
#     # T立つよりも先に端に到達してしまう場合
#     Bdist = (B + 10**9)
#   else:
#     # print("run left")
#     Bdist = W * T
# else:
#   # 正の方向に逃げる
#   if (10**9 - B) / W <= T:
#     # print("right reach")
#     Bdist = (10**9 - B)
#   else:
#     # print("run right")
#     Bdist = W * T

# Adist = V * T
# if Bdist + abs(A - B) <= Adist:
#   print("YES")
# else:
#   print("NO")
