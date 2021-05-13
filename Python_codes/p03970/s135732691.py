s = list(input())

t_s = list('CODEFESTIVAL2016')
n = len(t_s)
cnt = 0

for s1,s2 in zip(s,t_s):
    if s1 != s2:
        cnt += 1
print(cnt)



