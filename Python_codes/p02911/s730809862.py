n, k, q = map(int, input().split())
answers = []
for _ in range(q):
    answers.append(int(input()))

cnt_list = [(k-q)]*n
if q < k:
    for _ in range(n):
        print('Yes')
else:
    for i in answers:
        cnt_list[i-1] += 1
    for i in cnt_list:
        print('Yes') if i > 0 else print('No')