import collections
h , w = map(int,input().split())
p = []
for i in range(h):
    p.extend(list(input()))
c = collections.Counter(p)

if h % 2 == 0 and w % 2 == 0:
    for k , v in c.items():
        if v % 4 != 0:
            print("No")
            exit()
    print("Yes")
    
elif h % 2 != 0 and w % 2 != 0:
    m = 0
    n = 0
    for k , v in c.items():
        if v % 4 == 1:
            n += 1
            if n > 1:
                print("No")
                exit()
        elif v % 4 == 2:
            m += 1
            if m > w//2 + h//2:
                print("No")
                exit()
        elif v % 4 == 3:
            n += 1
            m += 1
            if n > 1:
                print("No")
                exit()
            if m > w//2 + h//2:
                print("No")
                exit()
        
    print("Yes")
elif h % 2 != 0:
    m = 0
    for k , v in c.items():
        if v % 4 == 1 or v % 4 == 3:
            print("No")
            exit()
        elif v % 4 == 2:
            m += 1
            if m > w//2:
                print("No")
                exit()
    print("Yes")
elif w % 2 != 0:
    m = 0
    for k , v in c.items():
        if v % 4 == 1 or v % 4 == 3:
            print("No")
            exit()
        elif v % 4 == 2:
            m += 1
            if m > h//2:
                print("No")
                exit()
    print("Yes")        