a, b, c, d, e = map(int, input().split())
start = a*60 + b
end = c*60 + d

print(end - e - start)