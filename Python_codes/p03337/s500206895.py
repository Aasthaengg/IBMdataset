a, b = map(int,input().split())

calArray = []
calArray.append(a+b)
calArray.append(a-b)
calArray.append(a*b)

result = sorted(calArray,reverse=True)

print(result[0])

