h,w= list(map(int, input().strip().split()))
grid = []
for i in range(h):
    array = input().strip()
    grid.append(array)
print('#'*(w+2))
for i in range(h):
    print("#"+grid[i]+"#")
print('#'*(w+2))