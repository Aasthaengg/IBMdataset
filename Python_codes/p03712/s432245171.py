#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]


h,w = map(int, input().split())
a = [list(input()) for _ in range(h)]

for i in range(h+2):
    for j in range(w+2):
        if (i == 0 or i == h+1):
            print("#", end="")
        else:
            if (j == 0 or j == w+1):
                print("#", end="")
            else:
                print(a[i-1][j-1], end="")
    print("")



