N, A, B = map(int, input().split())

if A % 2 == B % 2:
    print((B - A) // 2)
elif B - A == 1:
    print(min(B - 1, N - A))
else:
    a = ((B - (A - 1) - 1) - 1) // 2 + (A - 1) + 1
    b = (N - (A + (N - B) + 1)) // 2 + (N - B) + 1
    #print(a)
    #print(b)
    print(min(a, b))