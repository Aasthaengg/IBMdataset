a,b,c = map(int, input().split())

for i in range(a, 100000000, a):
    if i % b == c:
        print("YES")
        exit()

print("NO")