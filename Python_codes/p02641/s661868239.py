x,n=map(int,input().split())
s=list(map(int,input().split()))
for i in range(101):
    if x-i not in s:
        print(x-i)
        break
    elif x+i not in s:
        print(x+i)
        break      