A, B = [int(str) for str in input().strip().split()]
print(B - A if B % A else A + B)