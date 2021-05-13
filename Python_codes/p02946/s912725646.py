k,x = map(int,input().split()) #k個黒　x黒

result = []
for i in range(k):
    result.append(x+i)
    result.append(x-i)

result = list(set(result))
result.sort()
print(*result)