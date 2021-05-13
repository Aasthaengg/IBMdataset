n, a, b = map(int, input().split())
ans_min = 0 if a+b-n <0 else a+b-n
print(min(a, b), ans_min)