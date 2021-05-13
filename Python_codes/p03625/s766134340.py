def main():
    n = int(input())
    inlis = list(map(int, input().split()))
    indic = dict()

    for i in range(n):
        a = inlis[i]
        if a in indic:
            indic[a] += 1
        else:
            indic[a] = 1
    indic2 = sorted(indic.items(), key = lambda x:x[0], reverse=True)
    ans1 = 0

    for j in range(n):
        kazu = indic2[j][1]
        nagasa = indic2[j][0]
        if kazu >= 4 and ans1 == 0:
            print(nagasa ** 2)
            exit()
        elif kazu >= 2 and ans1 == 0:
            ans1 = nagasa
        elif kazu >= 2 and ans1 > 0:
            print(ans1 * nagasa)
            exit()
    print(0)
        



if __name__ == "__main__":
    main()