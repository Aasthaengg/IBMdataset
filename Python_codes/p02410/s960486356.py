box_a = []
box_b = []
tate, yoko = map(int, input().split())
[box_a.append( list(map(int, input().split())) ) for i in range(tate)]
[box_b.append( int(input()) ) for i in range(yoko)]

for i in range(tate):
    stuck = []
    [stuck.append(box_a[i][j]*box_b[j]) for j in range(yoko)]
    #print("DBG:: i={0} box_a={1} - box_b={2}".format(i, box_a, box_b))
    print(sum(stuck))