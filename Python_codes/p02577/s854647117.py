n=input()
k=0
for m in n:
  k += int(m) % 9
print("Yes" if k % 9 == 0 else "No")
