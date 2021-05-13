L = []
p = "No"
for i in range(3):
  a, b, c = map(str, input().split())
  L.append(a)
  L.append(b)
  L.append(c)
n = int(input())
for i in range(n):
  d = input()
  for j in range(9):
    if d == L[j]:
      L[j] = "×"
if (L[0] == "×" and L[8] == "×" and L[4] == "×") or (L[1] == "×" and L[7] == "×" and L[4] == "×") or (L[2] == "×" and L[6] == "×" and L[4] == "×") or (L[3] == "×" and L[5] == "×" and L[4] == "×"):
  p = "Yes"
elif (L[0] == "×" and L[1] == "×" and L[2] == "×") or (L[2] == "×" and L[5] == "×" and L[8] == "×") or (L[0] == "×" and L[3] == "×" and L[6] == "×") or (L[6] == "×" and L[7] == "×" and L[8] == "×"):
  p="Yes"
print(p)