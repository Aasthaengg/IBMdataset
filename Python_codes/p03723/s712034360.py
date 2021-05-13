A, B, C = [int(a) for a in input().split()]

count = 0

while 1:
    if A%2==0 and B%2==0 and C%2==0:
        if A==B and B==C:
            print(-1)
            exit()
        A_tmp = B//2 + C//2
        B_tmp = A//2 + C//2
        C_tmp = A//2 + B//2
        A, B, C = A_tmp, B_tmp, C_tmp
        count += 1
    else:
        break
print(count)