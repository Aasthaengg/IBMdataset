import sys
A,B,C,D = map(int,input().split())

if not (1 <= A <= 10 and 1 <= B <= 10 and 1 <= C <= 10 and 1 <= D <= 10):
    sys.exit()

if A + B > C + D:
    print('Left')
elif A + B == C + D:
    print('Balanced')
elif A + B < C + D:
    print('Right')