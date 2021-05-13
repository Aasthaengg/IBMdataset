x, a, b = map(int, input().split())
dis1 = abs(x-a)
dis2 = abs(x-b)
print('A' if dis1<dis2 else 'B')