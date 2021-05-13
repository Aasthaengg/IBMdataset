MM = input().split()
H = int(MM[0])
W = int(MM[1])
print('#'*(W+2))
for i in range(H):
  a = input()
  print('#'+a+'#')
print('#'*(W+2))