N = int(input())
s = [int(input()) for _ in range(N)]

tmp = sum(s)
if tmp%10 != 0:
    print(tmp)
else:
    m = [i for i in s if i % 10 != 0]
    if m == []:
        print(0)
    else:
        print(tmp-min(m))