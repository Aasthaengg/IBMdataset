A, B = input().split()
X = int(A + B)
ans = "No"
for i in range(1000):
  if (i * i) == X:
    ans = "Yes"
print(ans)
