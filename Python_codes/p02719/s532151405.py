#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [input() for _ in range(n)]

n,k= map(int, input().split())

tmp = n//k

a = abs(n-k*tmp)
b = abs(a-k)

print(min(a,b))



