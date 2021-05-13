n = int(input())
a = input()
b = input()
c = input()
cnt=0
for i in range(n):
        if a[i]==b[i] and b[i]==c[i]:
            pass
        elif a[i]==b[i] or a[i]==c[i] or b[i]==c[i]:
            cnt+=1
        else:
            cnt+=2
print(cnt)