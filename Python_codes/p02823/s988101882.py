import sys

N, A, B = map(int, input().split(' '))
if (B - A) % 2 == 0:
    print((B - A) // 2)
else:
    print(min((A+B-1)//2, (N*2-A-B+1)//2))