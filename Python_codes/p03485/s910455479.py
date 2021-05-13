a,b = map(int,input().split())
result = (a+b)/2
print(int(result)+1 if result % int(result) != 0 else int(result))