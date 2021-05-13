S,T=map(str,input().split())
A,B=map(int,input().split())
U=str(input())


ans=[A,B]

if U==S:
    ans=[A-1,B]
else:
    ans=[A,B-1]


print(*ans)
