N = int(input())

#文字数分aで埋める
#末尾をbにする
#一桁上の文字+1文字までは許容するルールで増加させていく

ans = [0 for _ in range(N)]
stop = [i for i in range(N)]

def ans_print(ans_list):
    ans = list()
    for a in ans_list:
        ans.append(chr(a+97)) #97でaが出る

    print(''.join(map(str, ans)))
    return 0

def ans_check(ans):
    max_in_ans = 0

    for i in range(1,N):
        if max_in_ans + 1 < ans[i]:
            ans[i-1] += 1
            ans[i] = 0
            return ans_check(ans)
        else:
            max_in_ans = max(max_in_ans,ans[i])
    else:
        return ans

if N == 1:
    print("a")
else:
    while 1:
        ans_check(ans)
        ans_print(ans)
        ans[-1] += 1
        if ans == stop:
            ans_print(ans)
            break
