a,b =map(int,input().split())
a%=3
b%=3
print("Possible" if not a or not b or not (a+b)%3 else "Impossible")