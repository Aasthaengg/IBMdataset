h,w=map(int,input().split())
s=[input()for i in range(h)]
for i in range(2*h):
    print(s[i//2])