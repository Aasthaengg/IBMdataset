n=int(input())
x=int(n//1.08)
print(x if n==int(x*1.08) else x+1 if n==int((x+1)*1.08) else ':(')