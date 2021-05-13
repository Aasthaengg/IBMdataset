a, b, c = list(map(int, input().split()))
r = 0

for i in range(b):
    r = (r+a)%b

    if (r == c):
        print("YES")
        exit()

print("NO")