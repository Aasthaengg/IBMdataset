h,w = map(int,input().split())
count = [0]*26
l = [input() for i in range(h)]
for i in l:
    for j in i:
        count[ord(j)-ord("a")] += 1

if h%2:
    if w%2:
        c = 0
        c2 = 0
        for i in count:
            if i%4:
                if i%2:
                    c2 += 1
                else:
                    c += 1
        if c <= w//2+h//2 and c2 == 1:
            print("Yes")
        else:
            print("No")
    
    else:
        c = 0
        for i in count:
            if i%4:
                if i%2:
                    print("No")
                    exit()
                else:
                    c += 1
        if c <= w//2:
            print("Yes")
        else:
            print("No")
else:
    if w%2:
        c = 0
        for i in count:
            if i%4:
                if i%2:
                    print("No")
                    exit()
                else:
                    c += 1
        if c <= h//2:
            print("Yes")
        else:
            print("No")
            
    else:
        for i in count:
            if i%4:
                print("No")
                exit()
        print("Yes")