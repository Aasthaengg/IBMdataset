H,W=map(int,input().split())
print('#'*(W+2))
[print('#'+input()+'#') for _ in range(H)]
print('#'*(W+2))