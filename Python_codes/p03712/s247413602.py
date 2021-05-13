h,w = [int(i) for i in input().split()]

print('#' * (w + 2))

for i in range(h):
  str = input()
  str = '#' + str + '#'
  print(str)

print('#' * (w + 2))
