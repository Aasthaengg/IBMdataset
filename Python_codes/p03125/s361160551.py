A, B = [int(a) for a in input().split(" ")]
print(A+B if B%A==0 else B-A)