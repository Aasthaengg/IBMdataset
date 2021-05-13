n=int(input())
thou=n//100
hund=(n-(thou*100))//10
ones=n-((thou*100)+(10*hund))
if (thou==7) or (hund==7) or (ones==7):
    print("Yes")
else:
  print("No")
