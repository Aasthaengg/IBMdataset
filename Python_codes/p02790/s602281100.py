#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))

a, b= map(int, input().split())

if a < b:
    for i in range(b):
        print(a, end="")
else:
    for i in range(a):
        print(b, end="")
print("")
