N = int(input())
for i in range(N):
    p = input()
    li = sorted([int(i) for i in p.split(" ")])
    if li[-1]**2 == li[-2]**2 + li[-3]**2:
        print("YES")
    else:
        print("NO")