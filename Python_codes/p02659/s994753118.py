a,b = input().split()
a = int(a)
b = int(b[0])*100+int(b[2:])
ans = (a*b)//100
print(ans)