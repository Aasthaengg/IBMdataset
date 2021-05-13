W=input()
n=0
while True:
    T=input()
    if T=="END_OF_TEXT":
        break
    small_T=list(T.split())
    for i in range(len(small_T)):
        if str.lower(small_T[i])==str.lower(W):
            n += 1
print(n)
