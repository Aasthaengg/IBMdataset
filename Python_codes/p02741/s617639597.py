K = int(input())
Ans = 0
if K == 4 or K == 6 or K == 9 or K == 10 or K == 14 or K == 21 or K == 22 or K == 25 or K == 26:
  Ans = 2
elif K == 28 or K == 30:
  Ans = 4
elif K == 8 or K == 12 or K == 18 or K == 20 or K == 27:
  Ans = 5
elif K == 16:
  Ans = 14
elif K == 24:
  Ans = 15
elif K == 32:
  Ans = 51
else:
  Ans = 1
  
print(Ans)