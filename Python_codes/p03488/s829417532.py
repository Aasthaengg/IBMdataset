import sys

def solve():
    input = sys.stdin.readline
    s = input().strip("\n")
    s += "T"
    lens = len(s)
    x, y = map(int, input().split())
    direc = 0 #0はx軸方向、１はy軸方向への移動
    move = 0
    init = True
    xPossible = {0}
    yPossible = {0}
    for i in range(lens):
        if s[i] == "F": move += 1
        else:
            if direc == 0: 
                newSet = set()
                for item in xPossible:
                    if init:
                        newSet |= {item + move}
                    else:
                        newSet |= {item + move}
                        newSet |= {item - move}
                xPossible = newSet
                #print("X:", xPossible)
                
            else: 
                newSet = set()
                for item in yPossible:
                    newSet |= {item + move}
                    newSet |= {item - move}
                yPossible = newSet
                #print("Y:", yPossible)
            move = 0
            direc = (direc + 1) % 2
            if init: init = False

    if x in xPossible and y in yPossible: print("Yes")
    else: print("No")

    return 0

if __name__ == "__main__":
    solve()
