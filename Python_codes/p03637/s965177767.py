n=int(input())
A=list(map(int,input().split()))
ans4 = 0
ans2 = 0
for a in A:
  if a % 4 == 0:
    ans4 += 1
  elif a % 2 == 0:
    ans2 += 1
ans2 = ans2-(ans2%2)
if (n-ans2)//2 <= ans4:
  print("Yes")
else:
  print("No")