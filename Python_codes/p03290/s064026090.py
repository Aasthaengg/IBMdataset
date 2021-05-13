def main():
    D,G = [int(x) for x in input().split()]
    min_cnt = 0
    bonus = []
    for i in range(D):
        p,c = [int(x) for x in input().split()]
        bonus.append((p,c))
        min_cnt += p
    # print(bonus)
    # print(min_cnt)

    for bit in range(1<<D):
        score = 0
        cnt = 0
        for i,(p,c) in enumerate(bonus):
            if (1<<i) & bit:
                score += 100*(i+1)*p+c
                cnt += p
        # print(bin(bit),i,score,cnt,min_cnt)
        if score >= G:
            min_cnt = min(min_cnt, cnt)
        else:
            for i in reversed(range(0,D)):
                if (1<<i) & bit:
                    continue
                pi,ci = bonus[i]
                for j in range(pi-1):
                    score += 100*(i+1)
                    cnt += 1
                    # print(bin(bit),i,j,p,c,score,cnt,min_cnt)
                    if score >= G:
                        # print('break')
                        min_cnt = min(min_cnt, cnt)
                        break
    print(min_cnt)

if __name__ == '__main__':
    main()