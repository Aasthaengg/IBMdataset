N = int(input())
A = list(map(int, input().split()))
A.sort()
a = A[0]
for i in A[1:]:
    if i - a == 0:
        print("NO")
        break
    else:
        a = i
else:
    print("YES")

