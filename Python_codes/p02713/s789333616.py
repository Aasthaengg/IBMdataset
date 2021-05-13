k = int(input())

def gcf(a,b):
    if a % b == 0 :
        return b
    return gcf(b, a%b)

def gcf3(a,b,c):
    f_ab = gcf(a,b)
    return gcf(f_ab,c)

ans = 0
for a in range(1,k+1):
    for b in range(a,k+1):
        for c in range(b,k+1):
            if a == b == c:
                ans += gcf3(a,b,c)
            elif a != b and b != c and a != c:
                ans += gcf3(a,b,c)*6
            else:
                ans += gcf3(a,b,c)*3
print(ans)
