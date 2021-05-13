# -*- coding : utf-8 -*-

A = list(input())
B = list(input())
C = list(input())
X = [A,B,C]
t = 0

while True:
  if X[t] == []:
    if t == 0:
      print("A")
      break
    elif t == 1 :
      print("B")
      break
    elif t == 2:
      print("C")
      break
  else:
    if X[t][0] == "a":
      X[t].remove(X[t][0])
      t = 0
    elif X[t][0] == "b":
      X[t].remove(X[t][0])
      t = 1
    elif X[t][0] == "c":
      X[t].remove(X[t][0])
      t = 2