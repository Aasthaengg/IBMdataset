H, W = input().split(' ')
H = int(H)
W = int(W)
print('#'*(W+2))
for i in range(H):
  s = input()
  print('#'+s+'#')
print('#'*(W+2))