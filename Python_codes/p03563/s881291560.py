R=int(input())
G=int(input())
a=abs(R-G)
if G>R:
    print(max(R,G)+a)
else:
    print(min(R,G)-a)