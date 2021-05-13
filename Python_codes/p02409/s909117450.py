house = [[[0 for i in range(10)] for i in range(3)] for i in range(4)]
n = int(input())
for i in range(n):
    input_4 = list(map(int,input().split()))
    house[input_4[0]-1][input_4[1]-1][input_4[2]-1] += input_4[3]
for i in range(4):
    for j in range(3):
        print('',' '.join(map(str,house[i][j])))
    if i != 3:
        print('#'*20)