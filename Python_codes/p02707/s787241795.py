N = int(input())
boss = [0] * N
A = map(lambda x:int(x) - 1, input().split())

for i in A:
    boss[i] += 1

print(*boss, sep='\n')