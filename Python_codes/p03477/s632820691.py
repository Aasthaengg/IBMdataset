la,lb,ra,rb = map(int,input().split())
if la+lb > ra+rb:
    print('Left')
elif la+lb < ra+rb:
    print("Right")
else:
    print("Balanced")