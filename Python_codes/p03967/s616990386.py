from itertools import accumulate
S = input()
dic =  {"g":0, "p":1}
# 最適なのはgpgpgpgpと出し続ける
# me g-g 0
# me g-p -1
# me p-g 1
# me p-p 0
# 相手がpのとき、pを出すほうが良い、相手がgのとき、pを出すほうが良い
# 従って、pが余っている状態のときは常に出し続けるのが良い
As = [dic[s] for s in S]
cnt = 0
for i,s in enumerate(S):
    a = i % 2
    b = dic[s]
    cnt += (a-b)
print(cnt)