import sys
A = "".join(sys.stdin.readlines())
A = A.splitlines()
A = list(map(int,A))
print((A[0]+A[1]) * A[2]//2)