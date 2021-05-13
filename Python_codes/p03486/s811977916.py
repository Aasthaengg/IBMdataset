S=list(map(lambda x:x,input()))
T=list(map(lambda x:x,input()))

S.sort()
T.sort(reverse=True)
if S<T:
    print("Yes")
else:
    print("No")
