x=int(input())
tmp=0
for i in range(10**9):
    tmp+=i
    if x<=tmp:
        print(i)
        break