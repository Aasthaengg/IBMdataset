n=int(input())
for i in range(n):
    hens=[int(i) for i in input().split(" ")]
    t=max(hens)
    hens.remove(t)
    if t**2==hens[0]**2+hens[1]**2:
        print("YES")
    else:
        print("NO")