from collections import Counter

n = int(input())

A = [int(i) for i in input().split()]
counts = Counter(A)
tmp = 0


# case1: すべてが0の場合
if len(set(A)) == 1 and A[0] == 0:
    print("Yes")
    quit()

# case2: nが3の倍数で、x^y^z == 0 となり、counts ==  x:n//3,y:n//3,z:n//3を満たす

if len(counts.items()) == 3 and n % 3 == 0:
    tmp = 0
    for x, k in counts.items():
        if k == n // 3:
            tmp ^= x
        else:
            print("No")
            quit()
    if tmp == 0:
        print("Yes")
        quit()
    else:
        print("No")
        quit()

# case3: nが3の倍数で、counts == x: 2*n//3,0: n//3 を満たす

if len(counts.items()) == 2 and n % 3 == 0:
    if counts.most_common()[1][0] == 0 and counts.most_common()[1][1] == n // 3:
        print("Yes")
        quit()
    else:
        print("No")
        quit()

print("No")
