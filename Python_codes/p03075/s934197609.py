a,b,c,d,e = [int(input()) for _ in range(5)]
k = int(input())

if abs(a-b) >k or abs(a-c) >k or abs(a-d) >k or abs(a-e) >k or abs(b-c) >k or abs(b-d) >k or abs(e-b) >k or abs(c-d) >k or abs(c-e) >k or abs(d-e) >k :
  print(":(")
else:
  print("Yay!")
