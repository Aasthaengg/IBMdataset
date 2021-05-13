n=int(input())
*a,=map(int, input().split( ))
simi=1
simi_od=1
for ai in a:
    simi*=3
    if ai%2==0:
        simi_od*=2
print(simi-simi_od)
