def main():
    h, a = map(int, input().split())
    kaisuu = h // a
    amari = h % a
    if amari > 0:
        print(kaisuu + 1)
    else:
        print(kaisuu)
    
if __name__ == "__main__":
    main()
