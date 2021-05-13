n = int(input())
Alist = list(map(int, input().split())) 

Blist = set(Alist)

if (len(Alist) - len(Blist)) % 2 ==0:
    print(len(Blist))
else:
    print(len(Blist)-1)