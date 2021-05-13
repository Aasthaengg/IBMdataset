s = str(input())
for i in range(1, 200):
    a = s[:-i]
    if len(s)%2 != 0:
        pass
    elif a[:len(a)//2] == a[len(a)//2:]:
        print(len(a))
        break
    else:
        pass