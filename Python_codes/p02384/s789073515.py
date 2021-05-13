dice = map(int, raw_input().split())

table = [ [1,2,4,3], # top:1
          [5,2,0,3], # top:2
          [1,5,4,0], # top:3
          [1,0,4,5], # top:4
          [0,2,5,3], # top:5
          [4,2,1,3]] # top:6

q = input()
for i in xrange(q):
    top, front = map(int, raw_input().split())
    tt = dice.index(top)          # get top side's index
    tf = dice.index(front)        # get front side's index
    tf = table[tt].index(tf) + 1  # get right side's index using talbe
    if tf > 3: tf = 0
    print dice[table[tt][tf]]