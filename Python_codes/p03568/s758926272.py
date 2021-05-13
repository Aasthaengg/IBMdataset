n = int(input())
A = list(map(int, input().split()))

print(3 ** n - 2 ** len([a for a in A if a % 2 == 0]))