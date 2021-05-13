n = int(input())
lst = list(map(int, input().split()))
rate = [400 * i for i in range(9)]
st = set()
rainbow = 0
for i in range(n):
  for j in range(8):
    if rate[j] <= lst[i] < rate[j + 1]:
      st.add(rate[j])
  if lst[i] >= 3200:
    rainbow += 1
if rainbow == n:
  print(1, n)
  exit()
print(len(st), len(st) + rainbow)