S = input()
Q = int(input())

prefix = ''
surfix = ''
cnt_reverse = 0

for i in range(Q):
    q = input()
    if q == '1':
        cnt_reverse += 1
    else:
        _, f, c = q.split()
        if (f=='1' and cnt_reverse%2==0):
            prefix = c + prefix
        elif (f=='2' and cnt_reverse%2==1):
            prefix = c + prefix
        elif (f=='1' and cnt_reverse%2==0):
            surfix = surfix + c
        else:
            surfix = surfix + c
if cnt_reverse % 2 == 0:
    S = prefix + S + surfix
else:
    S = surfix[::-1] + S[::-1] + prefix[::-1]
print(S)