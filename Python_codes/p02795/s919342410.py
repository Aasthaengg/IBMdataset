# キーエンス プログラミング コンテスト 2020: A – Painting
import math

h, w, n = [int(input()) for _ in range(3)]
a = max(h, w)
print(math.ceil(n / a))