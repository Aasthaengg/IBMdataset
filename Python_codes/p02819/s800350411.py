#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [input() for _ in range(n)]

x = int(input())

def sosu(x):
    for i in range(2, x):
        if (x % i == 0):
            return False
    return True

for i in range(x, 100000+5):
    if (sosu(i)):
        print(i)
        exit()


