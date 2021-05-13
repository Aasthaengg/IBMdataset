a,b,c=map(int,input().split())
if a > c:print(a-c,"",b)
elif a + b > c:print("0",b-c+a)
else:print("0 0")