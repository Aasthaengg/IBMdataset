def main():
    k, x = map(int, input().split())
    anslis = [x for x in range(x-k+1, x+k)]
    print(*anslis)

    
if __name__ == "__main__":
    main()
