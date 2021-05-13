A, B = map(int, input().split())
print("{}".format(0 if (A - 2*B <= 0) else A - 2*B))