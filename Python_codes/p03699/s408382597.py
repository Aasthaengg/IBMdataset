n = int(input())
s = [int(input()) for _ in range(n)]
s.sort()
flag = list(map(lambda x: False if x%10 == 0 else True, s))

if sum(s)%10==0:
    for i in range(n):
        if flag[i]:
            s.pop(i)
            print(sum(s))
            break
    else:
        print(0)
else:
    print(sum(s))