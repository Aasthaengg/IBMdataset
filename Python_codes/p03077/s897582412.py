from math import ceil
n = int(input())
st = set()
for i in range(5):
  st.add(int(input()))
print(ceil(n / min(st)) + 4)