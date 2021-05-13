h,w=map(int,input().split())
p=[input() for _ in range(h)]

print('#'*(w+2))
for i in range(h):
  print('#{}#'.format(p[i]))
print('#'*(w+2))