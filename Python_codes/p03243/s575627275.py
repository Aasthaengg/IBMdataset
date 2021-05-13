n = int(input())
for i in range(n,1111):
    i = str(i)
    if len(set(i))==1:
        print(i)
        break