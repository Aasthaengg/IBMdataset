if __name__ == "__main__":
    N, A, B = map(int, input().split())
    
    if (B - 1 - A) % 2 == 0:
        print("Borys")
    else:
        print("Alice")