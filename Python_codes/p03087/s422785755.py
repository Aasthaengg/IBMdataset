def main():
    n, q = map(int, input().split())
    s = input()
    indic = {}
    for i in range(q):
        l, r = map(int, input().split())
        indic[i] = [l, r]
    
    ruisekidic = {}
    tmp = 0
    
    for i in range(n):
        if i == 0:
            mae = s[0]
            ruisekidic[i] = 0
        else:
            if mae == "A" and s[i] == "C":
                tmp += 1
                ruisekidic[i] = tmp
                mae = s[i]
            else:
                ruisekidic[i] = tmp
                mae = s[i]
    for i in range(q):
        [l, r] = indic[i]
        if l > 0:
            print(ruisekidic[r-1] - ruisekidic[l-1])
        else:
            print(ruisekidic[r-1])


    
if __name__ == "__main__":
    main()
