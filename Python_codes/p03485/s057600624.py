a,b = map(int, input().split())
print((a+b)//2 if (a+b)/2-int((a+b)/2) <0.5 else (a+b)//2+1)