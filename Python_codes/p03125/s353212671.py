A, B = map(int, input().split())
print("{}".format(A + B if B % A == 0 else B - A))