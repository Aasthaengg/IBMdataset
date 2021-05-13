#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))

a = list(map(int, input().split()))

if (sum(a) <= 21):
    print("win")
else:
    print("bust")

