h, w = map(int, input().split())
arr = [''] * h
for i in range(h):
  arr[i] = input()
print('#' * (w + 2))
for e in arr:
  print("#" + e + "#")
print('#' * (w + 2))