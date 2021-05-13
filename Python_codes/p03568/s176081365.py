N = int(input())
A = list(map(int, input().split()))

a = 3 ** N

e = [i % 2 == 0 for i in A].count(True)

print(a-2**e)