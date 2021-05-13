A,B,C,K = map(int,input().split())
ans = (B - A) * (-1 if K % 2 == 0 else 1)
if ans > 10 ** 18:
    print("Unfair")
else:
    print(ans)