def main():
    n = int(input())
    indic = dict()
    ans = 0

    for _ in range(n):
        a = int(input())
        if a in indic:
            indic[a] += 1
        else:
            indic[a] = 1
    for k in indic:
        if indic[k] % 2 != 0:
            ans += 1
    
    print(ans)




if __name__ == "__main__":
    main()