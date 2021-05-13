def resolve():
    A, B, C = map(int, input().split())
    D = max(max(A, B), C)
    ans = (D * 3 - A - B - C)
    print(ans//2 if ans %2 == 0 else (ans+3)//2)
resolve()