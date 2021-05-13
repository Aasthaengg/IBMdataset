N = int(input())
f = 0
for k in range(N):
    A, B = map(int,input().split())
    if A == B:
        f += 1
        if f == 3:
            print("Yes")
            exit(0)
    else:
        f = 0
print("No")
