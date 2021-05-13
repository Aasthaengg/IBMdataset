def main():
    import math
    n = int(input())
    inlis = list(map(int, input().split()))
    indic = dict()
    total = 0

    for num in inlis:
        if num in indic:
            indic[num] += 1
        else:
            indic[num] = 1
    
    for k, v in indic.items():
        total += int(v * (v-1) / 2)
    
    for num in inlis:
        print(total - indic[num] + 1)





if __name__ == "__main__":
    main()