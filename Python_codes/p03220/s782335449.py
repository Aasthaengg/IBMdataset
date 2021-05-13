import sys
input = sys.stdin.readline

N = int(input())
T, A = map(int, input().split())

H = list(map(int, input().split()))

Th = [T-H[i]*0.006 for i in range(N)]
Td = [abs(Th[i]-A) for i in range(N)]
print(Td.index(min(Td))+1)
