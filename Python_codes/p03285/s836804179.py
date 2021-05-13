N = int(input())
x = int(N / 7)

for i in range(x + 1):
  one = 7 * (i)
  if (N - one) % 4 == 0:
    print("Yes")
    quit()
print("No")