N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

print(sorted([(abs(A - (T - h * 0.006)), i+1) for i,h in enumerate(H)])[0][1])