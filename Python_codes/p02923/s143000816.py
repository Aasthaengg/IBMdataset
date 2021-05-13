N = int(input())
H = list(map(int,input().split()))

s = ""

for i in range(N-1) :
    if H[i+1] <= H[i] :
        s += "t"
    else :
        s += "f"
ans = len( max((s.split("f"))) )

print(ans)