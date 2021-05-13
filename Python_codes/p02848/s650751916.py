alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
N = int(input())
S = input()

print(*[alphabet[(alphabet.index(s) + N) % 26] for s in S], sep='')