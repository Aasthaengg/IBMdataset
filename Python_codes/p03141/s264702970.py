n=int(input())
t,B=[],0
for _ in range(n):
    a,b=map(int,input().split())
    t.append(a+b)
    B+=b
t.sort(reverse=True)
print(sum(t[0:n:2])-B)