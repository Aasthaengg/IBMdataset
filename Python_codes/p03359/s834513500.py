import sys
A,B = map(int, input().split())

count = 0
for a in range(1,13,1):
    if a>A:
        break
    for b in range(1,32,1):
        if a==A and b > B:
            print(count)
            sys.exit()
        if a==b:
            count = count + 1

print(count)