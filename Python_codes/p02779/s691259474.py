N = int(input())
A = tuple(map(int, input().split()))
if len(set(A)) == len(A):
    print("YES")
else:
    print("NO")