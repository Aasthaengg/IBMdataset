a,v = map(int,input().split())
b,w = map(int,input().split())
t = int(input())
d = abs(a-b)
if w-v >= 0:
    print("NO")
else:
    if t*(v-w) >= d:
        print("YES")
    else:
        print("NO")