n = int(input())
a = map(int, input().split())

s = sorted(a, reverse=True)
print(sum(s[i//2] for i in range(1, n)))
