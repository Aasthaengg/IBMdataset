
a,b,c = input().split()

if a[-1:]==b[:1]:
    if b[-1:]==c[:1]:
        print("YES")
        exit()

print("NO")