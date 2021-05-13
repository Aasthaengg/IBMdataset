_, A, B, C, D = map(lambda n: int(n) - 1, input().split())
S = input()
if S.count("##", A, D):
    print("No")
elif C < D:
    print("Yes")
elif S.count("...", B - 1, D + 2):
    print("Yes")
else:
    print("No")