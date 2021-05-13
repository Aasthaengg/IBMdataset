import sys

N = int(input())
now = [0]*3
for i in range(N):
    a, b, c = map(int, input().split())
    val0 = a-now[0]
    val1 = abs(b-now[1]) + abs(c-now[2])
    
    while val1 < val0:
        val1 += 2
    if val1 != val0:
        print('No')
        sys.exit()
    now = [a, b, c]
print('Yes')
    
