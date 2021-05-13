N = input()
l = list(map(int,N))
i = 0
#ans = l[0] - 1 + (len(l)-1)*9 #暫定の答え

if int(N) < 9:
    ans  = int(N)

elif l.count(9) >= len(l)-1:
    if l[len(l)-1] != 9:
        spot = 8
    else:
        spot = min(l)
    ans = spot + (len(l)-1)*9

else:
    while True:
        if l[i] < 9 and i < len(l)-1:
            spot = l[i] - 1
            break
        else:
            i += 1 
    ans = spot + (len(l)-1)*9

print(ans)
