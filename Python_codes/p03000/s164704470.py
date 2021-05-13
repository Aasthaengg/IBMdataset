def main():
    n,x = map(int,input().split())
    l = list(map(int, input().split()))
    dist = 0
    count = 1
    for i in range(n):
        dist += l[i]
        if dist > x:
            break
        count += 1
    print(count)
    
if __name__ == "__main__":
    main()