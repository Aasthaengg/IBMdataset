n = int(input())
s = list(map(str,input().split()))
arare = [0,0,0,0]
#PWGY
for i in range(n):
  if s[i] == "P":
    arare[0] = "1"
  elif s[i] == "W":
    arare[1] = "1"
  elif s[i]== "G":
    arare[2] = "1"
  else:
    arare[3] = "1"
    
  if arare.count("1") == 4:
    print("Four")
    exit()
    
print("Three")

