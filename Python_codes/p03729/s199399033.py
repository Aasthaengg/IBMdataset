A,B,C = map(str,input().split())
judge = True
if A[-1] != B[0]:
    judge = False
if B[-1] != C[0]:
    judge = False
if judge:
    print("YES")
else:
    print("NO")