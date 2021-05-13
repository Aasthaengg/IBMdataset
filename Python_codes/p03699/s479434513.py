N = int(input())
s = [int(input()) for _ in range(N)]
s.sort()
su = sum(s)

if su%10 != 0:
    print(su)
    exit()
    
for i in s:
    if i%10 != 0:
        print(su - i)
        exit()
print(0)