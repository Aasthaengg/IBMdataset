n=int(input())
l=[int(input()) for i in range(n)]
res = sum(l)-max(l)//2
print(res)