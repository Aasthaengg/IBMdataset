N = int(input())
T,A = map(int, input().split())
H = list(map(int, input().split()))

L = [abs(A - T + h*0.006) for h in H]

print(L.index(min(L)) + 1)