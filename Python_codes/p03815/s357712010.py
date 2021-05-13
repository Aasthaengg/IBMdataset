N = int(input())
ans = N//11
ans1 = N % 11
if(ans1 >= 7):
  ans2 = ans * 2 + 2
elif(ans1 <= 6) and (ans1 >= 1):
  ans2 = ans * 2 + 1
else:
  ans2 = ans * 2
print(ans2)
