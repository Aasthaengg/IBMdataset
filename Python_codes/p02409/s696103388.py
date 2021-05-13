n = int(input())

a = [[[0 for iii in range(10)] for ii in range(3)] for i in range(4)]

for i in range(n):
    b, f, r, m = map(int, input().split())
    a[b - 1][f - 1][r - 1] += m

for i in range(4):
    for ii in range(3):
        for iii in range(10):
            print(" " + str(a[i][ii][iii]), end="")
        print()
    if i == 3: break
    print("####################")
