idx = int(input())
in_dict = {}

for i in range(idx):
    b, f, r, v = (int(x) for x in input().split())
    b -= 1
    f -= 1
    r -= 1
    in_dict[(b,f,r)] = in_dict.get((b,f,r),0) + v

for b in range(4):
    for f in range(3):
        for r in range(10):
            print(" ",end="")
            print(in_dict.get((b,f,r),0), end="")
        print("\n", end="")
    if b in range(3):print("#"*20)