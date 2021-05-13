k, t = list(map(int, input().split()))
a = list(map(int, input().split()))

largest = max(a)
print(max(largest-(k-largest+1), 0))