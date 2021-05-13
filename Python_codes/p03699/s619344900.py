n = int(input())
s = [int(input()) for i in range(n)]
l = [i for i in s if i % 10 != 0]
su = sum(s)
if su % 10 == 0:
    try:
        print(su - min(l))
    except:
        print(0)
else:
    print(su)