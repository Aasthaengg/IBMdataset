#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]
#a = [int(input()) for _ in range(n)]

s = input()

if (s[0] != "A"):
    print("WA")
    exit()

s = s[1:]

if (s[1:-1].count("C") != 1):
    print("WA")
    exit()

s = s.replace("C","")

if (s.islower()):
    print("AC")
else:
    print("WA")


