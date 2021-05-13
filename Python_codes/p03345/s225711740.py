a,b,c,k = map(int,input().split())
if k%2 == 0 and a-b <= 10**18:
    print(a-b)
elif k%2 != 0 and a-b <= 10**18:
    print(b-a)
"""
else:
    print("Unfair")
"""