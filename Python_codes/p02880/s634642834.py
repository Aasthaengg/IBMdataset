N = int(input())
flag=False
for i in range(1,10):
    if (N%i==0 and N/i<=9):
        flag=True
print("Yes" if flag else "No")
