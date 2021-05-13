#
K = int(input())
A = list(map(int, input().split()))

#
if A[-1]!=2:
    print(-1)
    exit()
if K>1 and A[-2]!=2 and A[-2]!=3:
    print(-1)
    exit()

#
min_n = 2
max_n = 3
for i in A[::-1][1:]:
    a = (min_n - 1)//i
    b = max_n//i
    if a==b:
        print(-1)
        exit()

    if min_n%i==0:
        pass
    else:
        min_n = min_n + (i - min_n%i)
    max_n = max_n - max_n%i + i - 1
    #print(min_n, max_n)

#
print(min_n, max_n)
