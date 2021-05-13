a = input()
b = input()
A = list(a)
B = list(b)
CNT = 0
for i in range (3):
  if A[i] == B[i]:
    CNT += 1
print(CNT)