import pprint
H,W=map(int,input().split())
import copy
lastraw=["#"]*(W+2)
field=[["#"]*(W+2)]
for i in range(H):
  field.append(["#"]+list(input())+["#"])
 
field.append(lastraw)
maxmoves=0
#print(field)
saved_field=copy.deepcopy(field)
 
for i in range(H):
  for j in range(W):
    field=copy.deepcopy(saved_field)
    goal_point=(0,0)
    [sy,sx]=[j+1,i+1]
    [gy,gx]=[0,0]
 
    queue=[[sy,sx]]
    tests = ((-1,0),(0, 1),(1, 0),(0, -1))
    moves=0
 
    if field[sx][sy]=='#':
      queue=[]
    else:
      field[sx][sy]=0
 
    while True:
      if len(queue)==0:
        maxmoves=max(maxmoves,moves-1)
        break
      queue_next = []
      moves += 1
      #pprint.pprint(field)
      for y, x in queue:
        for ny, nx in tests:
          ty, tx = y + ny, x + nx
          if field[tx][ty] == '.':
            field[tx][ty] = moves
            queue_next.append((ty, tx))
      queue = queue_next
      if goal_point in queue:
        break
        #pprint.pprint(field)
        maxmoves=max(maxmoves,moves)
print(maxmoves)