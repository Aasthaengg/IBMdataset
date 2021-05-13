A, B, C, D = map(int, input().split())
areaA = A*B
areaB = C*D
result = areaA if (areaA > areaB) else areaB
print(result)
