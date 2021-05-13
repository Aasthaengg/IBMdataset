n = int(input())
a = input()
b = input()
c = input()
cnt = 0
for i in range(n):
    c1,c2,c3=0,0,0

    if b[i] ==a[i] and c[i]==b[i]:
        pass

    elif b[i] ==a[i] or c[i]==b[i] or c[i] ==a[i]:

        cnt+=1
    else:
        cnt+=2

print(cnt)
