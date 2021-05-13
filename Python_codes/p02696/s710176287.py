A, B, N = map(int, input().split())
Ans = []
X = B * (N // B)
if X != 0:
    ans_1 = (A * (X - 1) // B) - A * ((X - 1) // B)
else:
    ans_1 = 0
ans_2 = (A * N // B) - A * (N // B)
Ans.append(ans_1)
Ans.append(ans_2)

print(max(Ans))