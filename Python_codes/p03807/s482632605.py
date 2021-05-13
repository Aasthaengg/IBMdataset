n = int(input())
lst = list(map(lambda x: int(x) % 2, input().split()))
print(['NO', 'YES'][lst.count(1) % 2 == 0])