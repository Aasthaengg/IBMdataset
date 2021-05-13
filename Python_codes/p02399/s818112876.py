a, b = [int(x) for x in input().split(" ")]
print('{0} {1} {2:.5f}'.format(int(a / b), a % b, float(a / b)))