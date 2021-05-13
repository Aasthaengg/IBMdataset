def LI(): return list(map(str, input().split()))


A = LI()

A.sort(reverse=True)
print(int(A[0] +A[1]) +int(A[2]))
