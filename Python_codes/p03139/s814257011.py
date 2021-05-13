num = list(map(int, input().split()))
a = min(num[1],num[2])
b = max(0,(num[1]+num[2]) - num[0])
print(a,b)