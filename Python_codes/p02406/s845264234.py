n = int(raw_input())

print "",

for i in range(1,n + 1):
    x = i
    if x % 3 == 0:
        print i,
    else:
        while x:
            if x % 10 == 3:
                print i,
                break
            x /= 10