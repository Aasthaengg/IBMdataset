H,W = map(int,input().split())
while not(H==0 and W==0):
    for i in range(H): print('#'*W);
    print()
    H,W = map(int,input().split())

