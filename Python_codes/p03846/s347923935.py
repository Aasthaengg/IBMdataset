from collections import Counter
n = int(input())
list_A = list(map(int, input().split()))
mod = pow(10, 9) + 7

list_Counter = list(Counter(list_A).items())
ans = 1
list_Counter.sort(key=lambda x:x[0])

if n % 2 == 0:
    for i in range(n//2):
        l = list_Counter[i]
        if l[0] != 2*i + 1 or l[1] != 2:
            ans = -1

    if ans == -1:
        print(0)
    else:
        print((2**(n//2))%mod)
else:
    if list_Counter[0][0] == 0 and list_Counter[0][1] == 1:
        for i in range(1, n//2+1):
            l = list_Counter[i]
            if l[0] != 2*i or l[1] != 2:
                ans = -1
    else:
        ans = -1

    if ans == -1:
        print(0)
    else:
        print((2**(n//2))%mod)

