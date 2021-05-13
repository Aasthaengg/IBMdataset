int_n = int(input())
li_a = list(map(int, input().split()))

answer = 0
for a in li_a:
    wk = a
    while wk % 2 == 0:
        wk = wk // 2
        answer += 1
print(answer)
