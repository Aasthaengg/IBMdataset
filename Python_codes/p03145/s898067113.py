def main():
    A, B, C = map(int, input().split())
    tri = sorted([A, B, C])
    print(tri[0]*tri[1]//2)
if __name__ == "__main__":
    main()