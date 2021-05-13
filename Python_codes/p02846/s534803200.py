import sys
import string
input = sys.stdin.readline

T1, T2 = map(int, input().split())
A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())

if A1 < B1 and A2 < B2:
    print(0)
    exit()
if A1 > B1 and A2 > B2:
    print(0)
    exit()
delta1 = T1 * A1 - T1 * B1
delta2 = T2 * A2 - T2 * B2
if (delta1 + delta2) / delta1 > 0:
    print(0)
    exit()
if delta1 + delta2 == 0:
    print('infinity')
    exit()
if delta1 % (delta1 + delta2) == 0:
    print(2 * abs(delta1 // (delta1 + delta2)))
else:
    print(2 * abs(delta1 // (delta1 + delta2)) - 1)

