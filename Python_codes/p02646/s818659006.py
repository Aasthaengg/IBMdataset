buf = list(map(int,input().split(" ")))
A,V = buf[0],buf[1]

buf = list(map(int,input().split(" ")))
B,W = buf[0],buf[1]

T = int(input())

if V <= W:
    print("NO")
    exit(0)
if (abs(A - B) / (V - W)) <= T:
    print("YES")
else:
    print("NO")