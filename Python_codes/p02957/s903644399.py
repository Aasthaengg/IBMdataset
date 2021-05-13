# input
A, B = map(int, input().split())

# check
if abs(A - B) % 2 == 1:
    print("IMPOSSIBLE")
else:
    K = (A + B) // 2
    print(K)