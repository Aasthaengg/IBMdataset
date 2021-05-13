noA, noL = list(map(int, input().split()))

ans = "No"

for i in range(noA+1):
    for j in range(noA+1):
        if (i+j) == noA:
            if ((i*2)+(j*4)) == noL:
                ans = "Yes"
                break
print(ans)