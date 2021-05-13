k, x = map(int, input().split())
start = x - (k-1)
end = x + (k-1)
if start <= -1000000:
    start = -1000000
if end >= 1000000:
    end = 100000
print(' '.join(map(str, list(range(start, end+1)))))