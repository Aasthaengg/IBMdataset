def main():
    import bisect
    n, k, q = map(int, input().split())
    indic = {}
    for _ in range(q):
        a = int(input())
        if a in indic:
            indic[a] += 1
        else:
            indic[a] = 1
    
    for i in range(n):
        if i+1 not in indic:
            tensuu = k - q
        else:
            tensuu = k - q + indic[i+1]
        if tensuu <= 0:
            print('No')
        else:
            print('Yes')
    


if __name__ == "__main__":
    main()
