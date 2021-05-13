#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))

a, b, k = map(int, input().split())

if (a > 0):
    if (a >= k):
        a -= k
        print (a,b)
        exit()
    else:
        k -= a
        a = 0

if (b > 0):
    if (b >= k):
        b -= k
        print(a,b)
        exit()
    else:
        b = 0


print(a,b)
