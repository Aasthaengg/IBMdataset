# どうせすぐにみつかる
n = int(input())

def gen_sequence(seed):
    yield seed
    last = seed
    while True:
        if last&1:
            last = last*3 + 1
        else:
            last = last//2
        yield last

mem = set([])
for i,x in enumerate(gen_sequence(n), 1):
    if x in mem:
        print(i)
        exit()
    mem.add(x)