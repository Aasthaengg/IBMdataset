N = int(input())

for i in range(26):
  if (N-i*4)% 7 == 0 and N>= i*4:
    print("Yes")
    exit()
print("No")
