h, w = map(int, input().split())
a = [input() for _ in range(h)]

for _ in range(w+2):
  print('#', end='')
print()
for i in a:
  print('#' + i + '#')
for _ in range(w+2):
  print('#', end='')
print()
