array = list(map(int, input().split()))
K = int(input())

maxABC = max(array)
maxIndex = array.index(maxABC)
array.pop(maxIndex)

print(sum(array) + maxABC * 2**K)
