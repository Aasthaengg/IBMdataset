def main():
    A, V = map(int, input().split())
    B, W = map(int ,input().split())
    T = int(input())
    
    if W < V:
        if abs(A - B) <= abs(W - V)*T:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")

if __name__ == "__main__":
    main()