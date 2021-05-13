from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

h,w=nii()

print('#'*(w+2))
for i in range(h):
  print('#'+input()+'#')
print('#'*(w+2))