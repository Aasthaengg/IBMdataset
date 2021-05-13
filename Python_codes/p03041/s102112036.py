n, k = [int(v) for v in input().split()]
s = list(input())
print('{}{}{}'.format(''.join(s[:k-1]), s[k-1].lower(), ''.join(s[k:])))
