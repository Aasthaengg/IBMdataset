n = list(input())

for i in range(len(n)):
  if n[i] != n[len(n)-i-1]:
    print("No")
    exit()
print("Yes")