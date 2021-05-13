#k = int(input())
#s = input()
#a, b = map(int, input().split())
#l = list(map(int, input().split()))

k = int(input())
a, b = map(int, input().split())

largest = b // k * k

if (largest < a):
    print("NG")
else:
    print("OK")
