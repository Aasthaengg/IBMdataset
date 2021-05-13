abc = list(map(int, input().split()))
abc.remove(max(abc))

print(sum(abc))