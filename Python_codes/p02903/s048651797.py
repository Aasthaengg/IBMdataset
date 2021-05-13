h, w, a, b = map(int,input().split())
for i in range(b):
    for j in range(a):
        print("0",end="")
    for j in range(w-a):
        print("1",end="")
    print()
for i in range(h-b):
    for j in range(a):
        print("1",end="")
    for j in range(w-a):
        print("0",end="")
    print()