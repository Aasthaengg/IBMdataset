#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

h, w = map(int, input().split())

s = []
for i in range(h):
    c = input()
    s.append(c)

#print(s)

for i in range(2*h):
    print(s[i//2])

