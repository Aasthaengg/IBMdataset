input()
a = list(map(int, input().split()))[::2]
print(sum(x % 2 == 1 for x in a))