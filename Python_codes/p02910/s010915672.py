
def main():
  dance = input()
  
  for i in range(0, len(dance)):
    if (i+1) % 2 == 0:
      if dance[i] == "R": 
        print("No")
        return 0
    else:
      if dance[i] == "L":
        print("No")
        return 0
  print("Yes")
  return 1

main()