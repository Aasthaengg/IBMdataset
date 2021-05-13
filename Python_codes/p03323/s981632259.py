a,b = map(int,input().split())
c = abs(a-b)
print("Yay!" if a+b+c <= 16 else ":(")