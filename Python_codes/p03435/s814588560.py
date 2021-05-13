C11, C12, C13 = map(int, input().split());
C21, C22, C23 = map(int, input().split());
C31, C32, C33 = map(int, input().split());

# a1 = 0と仮定して他を調整する
b1 = C11;
b2 = C12;
b3 = C13;

a2 = C21 - b1;
a3 = C31 - b1;

if (C22 == a2 + b2 and
    C23 == a2 + b3 and
    C32 == a3 + b2 and
    C33 == a3 + b3):
  print("Yes");
else:
  print("No");