n = int(input())
s, t = zip(*[input().split() for _ in range(n)])
x = input()

print(sum(map(int, t[s.index(x)+1:])))