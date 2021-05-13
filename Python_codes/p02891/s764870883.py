def f(S):
    all_cnt = 0
    cnt = 0
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            cnt += 1
        else:
            if cnt > 0:
                if cnt % 2 == 1:
                    all_cnt += (cnt + 1) / 2
                else:
                    all_cnt += cnt / 2
            cnt = 0
        # print(cnt,all_cnt)
    if cnt > 0:
        if cnt % 2 == 1:
            all_cnt += (cnt + 1) / 2
        else:
            all_cnt += cnt / 2
    return int(all_cnt)

def main():
    S = input()
    K = int(input())
    if S.count(S[0]) == len(S):
        print(len(S)*K // 2)
        return
    if S[-1] == S[0]:
        print((f(S + S) - f(S))*(K-1) + f(S))
    else:
        print(f(S)*K)

if __name__ == '__main__':
    main()