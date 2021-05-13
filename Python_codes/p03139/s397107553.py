N, A, B = map(int, input().split())
ResMax = min(A, B)
ResMin = max(0, A+B-N)
print(ResMax, ResMin)