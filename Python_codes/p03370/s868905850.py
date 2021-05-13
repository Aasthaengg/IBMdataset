n,m = map(int,input().split())
li = []
for i in range(n):
    a = int(input())
    li.append(a)
print(n+(m-sum(li))//min(li))