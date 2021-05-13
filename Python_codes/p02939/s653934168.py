S = list(input())
former = ''
tmp = []
count = 0
for i in range(len(S)):
    tmp.append(S[i])
    if not ''.join(tmp) == former:
        former = ''.join(tmp)
        tmp = []
        count += 1
print(count)
