N = int(input())
T, A = map(int, input().split())
H = map(int, input().split())
scores = {}
for i, h in enumerate(H, 1):
    scores[i] = abs (A - (T - h * 0.006))
print(min(scores, key=scores.get))