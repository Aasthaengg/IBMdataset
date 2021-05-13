n = int(input())
s = [int(input()) for _ in range(n)]
s.sort()

if sum(s)%10==0:
    for i in range(n):
        if s[i]%10!=0:
            s.pop(i)
            print(sum(s))
            break
    else:
        print(0)
else:
    print(sum(s))