
s = list(input())

k = int(input())

cnt = 0

if len(s) == 1:
    print(s[0])
else:
    if s[0] == "1":
        
        while s[0] == "1":
            cnt += 1
            del s[0]
            if cnt>=k:
                print(1)
                break
            
        if cnt<k:
            print(s[0])
            
    else:
        print(s[0])