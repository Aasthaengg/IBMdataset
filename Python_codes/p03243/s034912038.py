val = [111*i for i in range(1, 10)]
N = int(input())
while not N in val:
  N += 1
print(N)