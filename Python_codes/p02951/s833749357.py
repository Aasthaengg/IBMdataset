a,b,c = map(int, input().split())
print(0) if a-b-c >= 0 else print(abs(a-b-c))