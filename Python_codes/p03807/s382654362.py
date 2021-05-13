N = int(input())
A = list(map(int, input().split()))

if sum([A[i]%2==1 for i in range(N)])%2 == 0:
    print("YES")
else:
    print("NO")
