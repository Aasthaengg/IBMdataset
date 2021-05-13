K,X = map(int, input().split())
begin = max(-1000000, X-K+1)
end = min(1000000, X+K-1)
print(' '.join(list(map(str, range(begin, end+1)))))
