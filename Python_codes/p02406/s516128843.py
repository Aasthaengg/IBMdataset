n = int(input())
o = ""
for i in range(1, n+1):
    if (i % 3) == 0:
        o = o + " " + str(i)
    
    else:
        x = i
        while x >0:
            if (x % 10) == 3:
                o = o + " " + str(i)
                break
            x //= 10
    
print(o)