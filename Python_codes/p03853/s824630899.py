h, w = map(int, input().split())
c = [list(input().split()) for i in range(h)]

pic = []
for i in range(h):
    pic.append(c[i])
    pic.append(c[i])
    
for i in range(len(pic)):
    print(''.join(pic[i]))