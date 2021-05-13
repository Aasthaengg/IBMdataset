# -*- coding: utf-8 -*-
import math

#入力
A, B, C = map(str, input().split())

if (len(A) == 1) :
  Aend = A
else :
  Aend = A[len(A)-1:len(A)]

if (len(B) == 1) :
  Bstart = B
  Bend = B
else :
  Bstart = B[0:1]
  Bend = B[len(B)-1:len(B)]

Cstart = C[0:1]

if Aend == Bstart and Bend == Cstart :
  print ("YES")
else :
  print ("NO")
