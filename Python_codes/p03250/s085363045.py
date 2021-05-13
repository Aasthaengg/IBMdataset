a,b,c = map(int,input().split())

h = a + b + c
i = max(a,b,c)
j = i * 10
print(j + h - i)    