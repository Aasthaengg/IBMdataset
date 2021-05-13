#k = int(input())
#s = input()
#a, b = map(int, input().split())
#l = list(map(int, input().split()))
a, b, c, k = map(int, input().split())

if (k<=a):
    print(k)
    exit()

# kがaより多い

if (k - a <= b):
    print (a)
    exit()

# kがa+bより多い

print (a - (k -(a+b) ))




