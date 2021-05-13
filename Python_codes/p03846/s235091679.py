from collections import Counter

N= int(input())
Alist = list(map(int, input().split())) 

count = Counter(Alist)
res = 1
if N % 2 ==0:
    for i in range(1,N,2):
        if count[i] != 2:
            print(0)
            exit()
else:
    if count[0] != 1:
        print(0)
        exit()
    else:
        for i in range(2,N,2):
            if count[i] != 2:
                print(0)
                exit()
print(2**(N//2) % (10**9+7))