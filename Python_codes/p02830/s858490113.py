n = int(input())
s, t = input().split()
res = [a + b for a, b in zip(s, t)]
print(''.join(res))