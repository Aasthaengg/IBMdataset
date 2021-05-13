#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [input() for _ in range(n)]

n = int(input())
l = list(map(int, input().split()))

l.sort()
if (l[-1] < sum(l[0:-1])):
    print("Yes")
else:
    print("No")





