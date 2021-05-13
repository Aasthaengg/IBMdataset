X, Y = map(int, input().split())

ans1, ans2, ans3=X+Y, X-Y, X*Y
if (ans1>=ans2 and ans1>=ans3):
  print(X+Y)

elif(ans2>=ans1 and ans2>=ans3):
  print(X-Y)

else:
  print(X*Y)
