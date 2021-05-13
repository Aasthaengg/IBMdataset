X=int(input())

ans=''
for a in range(-125,125):
    for b in range(-125,125):
        i = a**5-b**5
        if i == X:
            ans=[a,b]
print(' '.join(map(str,ans)))