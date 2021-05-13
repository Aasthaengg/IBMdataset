n = int(input())
abc = [int(input()) for _ in range(5)]
bot = min(abc)
print((n + bot - 1) // bot + 4)