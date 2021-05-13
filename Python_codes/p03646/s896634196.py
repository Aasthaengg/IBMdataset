K = int(input())
a, roop = K % 50, K // 50
if roop >= 1:
    Ans = [50 + roop] * a + [50 - a + roop - 1] * (50-a)
else:
    Ans = [100 - a] * a + [49 - a] * (50 - a)
print(50)
print(" ".join(map(str, Ans)))