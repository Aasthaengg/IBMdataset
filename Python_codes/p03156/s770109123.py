# AISing Programming Contest 2019 / エイシング プログラミング コンテスト 2019: B – Contests
N = int(input())
A, B = [int(s) for s in input().split()]
P = [int(s) for s in input().split()]

leA = [p for p in P if p <= A]
gtAleB = [p for p in P if A < p <= B]
gtB = [p for p in P if p > B]

print(min(len(leA), len(gtAleB), len(gtB)))