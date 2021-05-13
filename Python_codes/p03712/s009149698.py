def resolve():
    h, w = map(int, input().split())

    image = list()
    image_line = ""
    for i in range(h):
        image_line = input()
        image_line = "#" + image_line + "#"
        image.append(image_line)

    sharp_line = ""
    for i in range(w + 2):
        sharp_line += "#"
    
    image.insert(0, sharp_line)
    image.append(sharp_line)

    for i in range(h + 2):
        print(image[i])
resolve()