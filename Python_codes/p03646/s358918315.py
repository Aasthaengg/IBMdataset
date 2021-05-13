K=int(input())
q=K//50
r=K%50
A=[49+q-r for i in range(50-r)]
B=[100+q-r for i in range(r)]
ans=A+B
print(50)
print(*ans)
