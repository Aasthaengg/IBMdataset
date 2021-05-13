H,W=map(int,input().split())
print(''.join(['#'for i in range(W+2)]))
for i in range(H):print('#'+input()+'#')
print(''.join(['#'for i in range(W+2)]))