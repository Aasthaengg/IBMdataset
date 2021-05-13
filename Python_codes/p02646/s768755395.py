A ,V = map(int ,input().split())
B ,W = map(int ,input().split())
T = int(input())
if A != B and V <= W:
    print("NO")
elif max(A - B,B - A) / (V - W) <= T:
    print("YES")
else:
    print("NO")