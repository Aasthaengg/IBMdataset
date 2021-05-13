a, b, c, d = map(int,input().split())
print(["RLiegfhtt"[a+b > c+d::2], "Balanced"][a+b == c+d])