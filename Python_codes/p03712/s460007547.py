H,W = map(int,input().split())
print('#'*(W+2))
for i in range(H):
    pixel = input()
    print(f'#{pixel}#')
print('#'*(W+2))