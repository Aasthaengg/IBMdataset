N = int(input())
A = list(map(int, input().split()))
print(3 ** N - 2 ** sum([1 for i in A if not i % 2]))