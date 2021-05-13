a,b = map(int, input().split())

left = a - (b*2)
print(left) if left >= 0 else print('0')