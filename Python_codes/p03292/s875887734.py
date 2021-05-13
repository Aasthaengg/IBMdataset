import sys
A1,A2,A3 = map(int,input().split())
array_A = [A1,A2,A3]

if not (1 <= A1 <= 100 and 1 <= A2 <= 100 and 1 <= A3 <= 100):
    sys.exit()

print(max(array_A) - min(array_A))