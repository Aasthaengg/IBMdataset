n = int(input())
li = list(map(int,input().split()))
lee = len(li)
base = 1
for l in li:
    if l%2 == 0:
        base*=2
print(3**lee-base)