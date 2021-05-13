A_college = [[[0 for _ in range(10)] for _ in range(3)] for _ in range(4)]

N = int(input())
moves = [[int(i)-1 for i in input().split()] for _ in range(N)]

for m in moves:
    b,f,r,v = m
    v += 1
    A_college[b][f][r] += v

for b,building in enumerate(A_college):
    if 0 != b: print('#'*20)
    for flr in building:
        print('',*flr)
