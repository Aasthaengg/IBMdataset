n = int(input())
temp = (n // 100) * 111
print(temp if temp >= n else temp + 111)