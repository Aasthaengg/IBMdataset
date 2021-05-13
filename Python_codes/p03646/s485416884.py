K=int(input())
a=K%50
b=K//50
l=[49+b-a]*(50-a)+[100+b-a]*a
print(50)
print(*l)