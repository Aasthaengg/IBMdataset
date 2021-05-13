N = int(input())
flag=0
for i in range(26):
    for j in range(16):
        if i*4+j*7==N:
            flag=1
print("Yes"if flag==1 else "No")