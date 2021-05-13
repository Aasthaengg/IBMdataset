n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
sa = sum(a)
sb = sum(b)
counta = 0
countb = 0
for i,j in zip(a,b):
    if j > i:
        if (j-i)%2:
            countb += 1
        counta += (j-i+1)//2
    elif i > j:
        countb += i-j
if counta <= sb-sa and countb <= sb-sa:
    print("Yes")
else:
    print("No")
