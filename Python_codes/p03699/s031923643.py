n=int(input())
s = [int(input()) for _ in range(n)]
s.sort()
if sum(s) %10 !=0:
    print(sum(s))
    exit()
else:
    for i in range(n):
        if s[i] %10 != 0:
            print(sum(s) - s[i])
            exit()
        else:
            continue
print(0)