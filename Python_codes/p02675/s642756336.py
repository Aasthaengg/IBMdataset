moji = str(input())[-1]
if int(moji) == 3:
    print("bon")
else:
    print(("hon","pon")[int(moji) in [0,1,6,8]])