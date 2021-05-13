import sys
N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

temp = list(map(lambda x: abs(A - (T - x*0.006)), H))
print(temp.index(min(temp))+1)