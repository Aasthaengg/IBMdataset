T1, T2 = map(int, input().split())
A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())
flag = False
if ((T1*A1 > T1*B1) and (T1*A1 + T2*A2 <= T1*B1 + T2*B2)) or ((T1*A1 < T1*B1) and (T1*A1 + T2*A2 >= T1*B1 + T2*B2)):
  flag = True

if flag:
  a1 = abs(T1*A1 - T1*B1)
  a2 = abs(T1*A1+T2*A2-T1*B1-T2*B2)
  if a2 == 0:
    print("infinity")
  else:
    b1 = a1//a2
    b2 = a1 % a2
    if b2 == 0:
      print(a1//a2*2)
    else:
  	  print(1 + a1//a2*2)
else:
  print(0)