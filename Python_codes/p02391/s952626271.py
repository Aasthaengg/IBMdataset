ia=[int(i) for i in input().split(" ")]
print("a < b" if ia[0]<ia[1] else "a > b" if ia[0]>ia[1] else "a == b")