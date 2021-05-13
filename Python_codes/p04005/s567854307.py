def main():
    A,B,C=map(int,input().split())
    print(min(A%2*B*C,B%2*A*C,C%2*A*B))

main()