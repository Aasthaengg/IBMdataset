dice = {
    '1': {'F':'2', 'R':'4', 'B':'5', 'L':'3'},
    '2': {'F':'6', 'R':'4', 'B':'1', 'L':'3'},
    '3': {'F':'6', 'R':'2', 'B':'1', 'L':'5'},
    '4': {'F':'6', 'R':'5', 'B':'1', 'L':'2'},
    '5': {'F':'6', 'R':'3', 'B':'1', 'L':'4'},
    '6': {'F':'5', 'R':'4', 'B':'2', 'L':'3'}
}

faces = list(map(int, input().split()))
q = int(input())

rightSide = {'F':'L','R':'F','B':'R','L':'B'}

for i in range(q):
    top, front = list(map(int, input().split()))
    topIdx = str(faces.index(top) + 1)
    frontIdx = str(faces.index(front) + 1)
    for k,v in dice[topIdx].items():
        if v[0] == str(frontIdx):
            faceIdx = dice[topIdx][rightSide[k]]
            print(faces[int(faceIdx)-1])
            break