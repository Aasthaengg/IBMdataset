n=int(input())

latest_dic = {}
array   = []
answers = []

for i in range(n):
    c = int(input())
    array.append(c)

for i,c in enumerate(array):
    if i==0:
        answers.append(1)
        latest_dic[c] = 1
    else:
        cnt = answers[i-1]
        if (c in latest_dic) and (c!=array[i-1]):
            cnt += latest_dic[c]
            answers.append(cnt)
        else:
            answers.append(cnt)
        latest_dic[c]=cnt

print(answers[n-1]%(10**9 +7))
