label = input().split()
rot = input()

dice = {
        "top":1,
        "front":2,
        "right":3,
        "left":4,
        "back":5,
        "bottom":6
        }

for r in rot:
    if r == 'E':
        t = dice["top"]
        dice["top"] = dice["left"]
        dice["left"] = dice["bottom"]
        dice["bottom"] = dice["right"]
        dice["right"] = t
    elif r == 'N':
        t = dice["top"]
        dice["top"] = dice["front"]
        dice["front"] = dice["bottom"]
        dice["bottom"] = dice["back"]
        dice["back"] = t
    elif r == 'S':
        t = dice["top"]
        dice["top"] = dice["back"]
        dice["back"] = dice["bottom"]
        dice["bottom"] = dice["front"]
        dice["front"] = t
    elif r == 'W':
        t = dice["top"]
        dice["top"] = dice["right"]
        dice["right"] = dice["bottom"]
        dice["bottom"] = dice["left"]
        dice["left"] = t
print(label[dice["top"]-1])