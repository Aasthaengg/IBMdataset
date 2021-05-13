h,  w =  map(int, input().split())
a = []
a.append("#"*(w+2))
for _ in  range(h):
    a.append("#"+input()+"#")
a.append("#"*(w+2))
print(*a, sep="\n")