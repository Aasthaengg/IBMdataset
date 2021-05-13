import itertools
A = list(map(int, input().split()))
s = sum(A)
A.sort()
for k in range(len(A)):
    li = list(itertools.combinations(A, k+1))
    for j in range(len(li)):
        if 2 * sum(li[j]) == s:
            print("Yes")
            break
    else:
        continue
    break
else:
    print("No")