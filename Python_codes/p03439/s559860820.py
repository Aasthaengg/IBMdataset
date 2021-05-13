from sys import stdin
N = int(stdin.readline().rstrip())
r = N-1
l = 0
print(0)
s = input()
cnt = 0
mid = (r+l)//2
if s == "Male":
    for _ in range(25):
        print(mid)
        s = input()
        if s == "Male" and mid % 2 == 0:
            l += max((r-l)//2,1)
        elif s == "Female" and mid % 2 != 0:
            l += max((r-l)//2,1)
        elif s == "Vacant":
            break
        else:
            r -= max((r-l)//2,1)
        mid = (r+l)//2
        
elif s == "Female":
    for _ in range(25):
        print(mid)
        s = input()
        if s == "Female" and mid % 2 == 0:
            l += max((r-l)//2,1)
        elif s == "Male" and mid % 2 != 0:
            l += max((r-l)//2,1)
        elif s == "Vacant":
            break
        else:
            r -= max((r-l)//2,1)
        mid = (r+l)//2