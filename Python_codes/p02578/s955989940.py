N = int(input())
As = input().split()

highest = 0
total = 0

for A in As:
  highest = max(int(A), highest)
  total += highest - int(A)

print(total)