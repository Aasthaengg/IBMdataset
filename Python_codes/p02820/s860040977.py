import sys
input = sys.stdin.readline

n, k = list(map(int, input().split()))
r, s, p = list(map(int, input().split()))
t = list(input())

safe = [False] * n

result = [True] * n

for i in range(n-k):
    if t[i] == t[i+k] and (not safe[i]):
        result[i] = False
        safe[i+k] = True


points = {"r":p, "s":r, "p":s}

score = 0

for i in range(n):
    if result[i]:
        score += points[t[i]]

print(score)
