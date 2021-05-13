#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]



s = input()

last = ""
for i in s:
    if (last == i):
        print("Bad")
        exit()
    last = i
print("Good")
