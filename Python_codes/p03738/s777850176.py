#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]

a = input()
b = input()

al = len(a)
bl = len(b)

if (al > bl):
    print("GREATER")
elif (al < bl):
    print("LESS")
else:
    for i in range(al):
        if a[i] > b[i]:
            print("GREATER")
            exit()
        elif a[i] < b[i]:
            print("LESS")
            exit()
    print("EQUAL")
