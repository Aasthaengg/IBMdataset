N=int(input())
for i in range(26):
    for j in range(13):
        if i*4+j*7==N:
            print("Yes")
            exit()
print("No")
