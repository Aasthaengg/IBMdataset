def main(A,B):
    return A + B if (B % A == 0) else B - A

A,B = map(int,input().split())
print(main(A,B))