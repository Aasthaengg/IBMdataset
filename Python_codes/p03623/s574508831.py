#n = int(input())
#a = int(input())
#ls = list(input().split(" "))
#ls = list(map(int,input().split(" ")))
x,a,b = list(map(int,input().split(" ")))
#string = input()

distA = abs(x - a)
distB = abs(x - b)

if distA >= distB:
  print("B")
else:
  print("A")
