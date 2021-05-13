a, b = map(int,input().split())
result =a+b

if result > 24:
    print(result-24)
elif result == 24:
    print(0)
else:
    print(result)