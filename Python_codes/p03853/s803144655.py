h,w = map(int,input().split())
picture = []
for i in range(h):
    c = list(input())
    picture.append(c)
    picture.append(c)

for j in range(2*h):
    print("".join(picture[j]))