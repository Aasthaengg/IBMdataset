N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
l = [T - h*0.006 for h in H]
print(l.index(min(l, key=lambda v: abs(A - v))) + 1)