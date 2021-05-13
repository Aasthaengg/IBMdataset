def draw(h, w):
    print("#" * w)
    for i in range(h-2):
        print("#" + ("."*(w-2)) + "#")
    print("#" * w)
    print("")
 
while True:
    h, w = map(int, raw_input().split())
    if h == 0 and w == 0:
        break
    draw(h, w)