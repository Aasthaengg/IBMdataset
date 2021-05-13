N = int(input())
a = list(map(int,input().split()))

xor = 0
for i in a:
    xor ^=i

for i in a:
    print(xor^i)