a, b, c = map(int, input().split())
s = [a, b, c]
m = max(s)
s.remove(m)
print(sum(s))