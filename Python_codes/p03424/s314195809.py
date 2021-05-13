n=int(input())
s=list(map(str,input().split()))

s_1=set(s)
if len(s_1)==4:
    print("Four")
else:
    print("Three")