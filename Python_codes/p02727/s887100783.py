x,y,a,b,c=map(int,input().split())
reds=sorted(list(map(int,input().split())))
greens=sorted(list(map(int,input().split())))
neutral=sorted(list(map(int,input().split())))

reds=reds[a-x:]
greens=greens[b-y:]
total=sorted(reds+greens+neutral)

print(sum(total[len(total)-x-y:]))
