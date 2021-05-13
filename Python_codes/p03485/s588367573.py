a, b = map(int, input().split())
print(int((a+b)/2) if (a+b)%2==0 else int((a+b+1)/2))