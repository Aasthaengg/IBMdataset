a , b , c , k = map(int,input().split())
if k % 2 == 0:
    ans = a-b
elif k % 2 == 1:
    ans = b-a

if abs(ans) > 10 **18:
    print("Unfair")
elif abs(ans) <= 10**18:
    print(ans)