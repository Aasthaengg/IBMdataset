S = input()
K = int(input())
if S[:K].count("1") == K:
    print(1)
    exit()
A = S.lstrip("1")
print(A[0])