#N = int(input())
h = [int(x) for x in input().split()]
for i in range(3):
    if h[i] + h[(i+1)%3] == h[(i+2)%3]:
        print("Yes")
        exit()
print("No")