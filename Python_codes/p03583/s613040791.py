def main():
    N = int(input())
    for n in range(1, 3501):
        for h in range(1, 3501):
            denom = 4*n*h - N*n - N*h
            if denom == 0:
                continue
            w = (N*h*n) / denom
            if w == int(w) and w > 0:
                print(int(n), int(h), int(w))
                return
    
if __name__ == "__main__":
    main()
