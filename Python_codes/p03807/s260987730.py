N = int(input())
As = input().split()

c_even = 0
c_odd = 0

for A in As:
  if int(A)%2 == 0:
    c_even += 1
  else:
    c_odd += 1

if c_even != 0 and c_odd%2 != 0:
  print("NO")
  exit(0)
print("YES")