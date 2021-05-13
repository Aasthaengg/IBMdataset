#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))

k = int(input())

for i in range(1,10):
    if (k % i == 0):
        if (k // i < 10):
            print("Yes")
            exit()
print("No")


