A,B = (int(x) for x in input().split())

result = [A+B,A-B,A*B]

print(max(result))