'''
参考
https://ikatakos.com/pot/programming_algorithm/contest_history/atcoder/2019/0817_agc037
'''

S = input()

pre = ''
ans = 0
cnt = 0

while cnt < len(S):
    ch = S[cnt]
    if ch == pre:
        cnt += 1
        if cnt == len(S):
            break
        ch += S[cnt]
    pre = ch
    ans += 1
    cnt += 1

print(ans)
