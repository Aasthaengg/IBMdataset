def main():
    p=sorted(int(input()) for _ in range(int(input())))
    p[-1] //= 2
    print(sum(p))
    
if __name__ == "__main__":
    main()