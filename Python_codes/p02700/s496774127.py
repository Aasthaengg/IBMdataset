#k = int(input())
#s = input()
#a, b = map(int, input().split())
#l = list(map(int, input().split()))
a,b,c,d= map(int, input().split())

while 1:
    c = c -b
    if (c <= 0):
        print("Yes")
        exit()
    a = a - d
    if (a <= 0):
        print("No")
        exit()


