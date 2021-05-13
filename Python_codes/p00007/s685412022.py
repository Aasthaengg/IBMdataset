n = int(raw_input())
total = 100000
for i in range(1,n+1):
    total = total*1.05
    if total%1000!=0:
        total = int(total-total%1000 + 1000)
    else:
        total = int(total)
print total