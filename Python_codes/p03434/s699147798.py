#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]
#a = [int(input()) for _ in range(n)]

n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

ali = 0
bob = 0

for i in range(n):
    if i % 2 == 0:
        ali += a[i]
    else:
        bob += a[i]
print(ali-bob)






