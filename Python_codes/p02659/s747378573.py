A, B = map(float, input().split())
A = int(A)
B = round(B*100)
mul = A * B
answer = mul // 100
print(answer)