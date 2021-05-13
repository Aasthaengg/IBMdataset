A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
A3 = list(map(int, input().split()))
N = int(input())
R = []
for i in range(N):
  S = int(input())
  R.append(S)

if A1[0] in R and A2[1] in R and A3[2] in R:
  print("Yes")
elif A1[2] in R and A2[1] in R and A3[0] in R:
  print("Yes")
elif A1[0] in R and A1[1] in R and A1[2] in R:
  print("Yes")
elif A2[0] in R and A2[1] in R and A2[2] in R:
  print("Yes")
elif A3[0] in R and A3[1] in R and A3[2] in R:
  print("Yes")
elif A1[0] in R and A2[0] in R and A3[0] in R:
  print("Yes")
elif A2[1] in R and A2[1] in R and A3[1] in R:
  print("Yes")
elif A1[2] in R and A2[2] in R and A3[2] in R:
  print("Yes")
else:
  print("No")