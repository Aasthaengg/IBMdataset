from collections import deque

n,k = map(int, input().split())
al = list(map(int, input().split()))
al_sum = sum(al)

al_divs = []
for i in range(1, int(al_sum**0.5)+1):
    if al_sum%i == 0:
        al_divs.append(i)
        if i*i != al_sum:
            al_divs.append(al_sum//i)

al_divs.sort(reverse=True)
for div in al_divs:
    # al_rems = [0]*div
    al_rems = []
    for a in al:
        # al_rems[a%div] += 1
        al_rems.append(a%div)
    al_rems.sort()
    cnt = 0
    curr_num = 0
    q = deque(al_rems)
    while q:
        if curr_num >= 0:
            l = q.popleft()
            cnt += l
            curr_num -= l
        else:
            r = q.pop()
            cnt += (div-r)
            curr_num += (div-r)
    # print('---',div)
    # print(cnt)
    if cnt//2 <= k:
        print(div)
        break