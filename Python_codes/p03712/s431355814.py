H,W=map(int,input().split())
print('#'*(W+2))
for i in range(H):
  print('#',end='')
  print(str(input()),end='')
  print('#')
print('#'*(W+2))