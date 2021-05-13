while True:
    line = list(map(int,input().split()))
    if line==[0,0]: break
    for i in range(line[0]): print('#'*line[1])
    print()