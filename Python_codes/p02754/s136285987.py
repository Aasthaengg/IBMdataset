N, A, B = map(int, input().split())
temp = N // (A+B)
temp2 = N % (A + B)
temp2 = min(temp2, A)
print(temp*A + temp2)