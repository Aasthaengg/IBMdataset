#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]
#a = [input() for _ in range(n)]


n = input()

for i in range(3):
    if n[i] == "9":
        print("1",end="")
    else:
        print("9",end="")
