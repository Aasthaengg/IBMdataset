a,b,c = list(map(int,input().split()))

sound_max = b//a

if c >= sound_max:
    print(sound_max)

elif c <= sound_max:
    print(c)


