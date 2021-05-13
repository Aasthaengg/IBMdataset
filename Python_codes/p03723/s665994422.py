import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8') 
inf = float('inf') ;mod = 10**9+7 
mans = inf ;ans = 0 ;count = 0 ;pro = 1

a, b, c = map(int, input().split())
state = [[a,b,c]]
if a%2 == 0  and a == b  and b == c:
    print(-1)
else:
    while True:
        if a%2==1 or b%2==1 or c%2==1:
            print(count)
            exit()
        a_2 = a//2
        b_2 = b//2
        c_2 = c//2
        a = b_2 + c_2
        b = a_2 + c_2
        c = a_2 + b_2
        if [a,b,c] in state:
            print(-1)
        else:
            state.append([a,b,c])
            count += 1