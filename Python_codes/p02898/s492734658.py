n, k = map(int, input().split())
a = [int(x) for x in input().split()]

print(len(list(filter(lambda x : x >= k, a))))