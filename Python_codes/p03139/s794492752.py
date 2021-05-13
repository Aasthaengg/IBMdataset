# 全国統一プログラミング王決定戦予選/NIKKEI Programming Contest 2019: A – Subscribers
n, a, b = map(int, input().split())
print(min(a, b), a + b - n if n <= a + b else 0)