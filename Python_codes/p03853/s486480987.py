h,w =list(map(int,input().split()))
c =[input() for i in range(h)]
d = []
for ih in range(2*h):
    print(c[ih//2])