x,y=map(int,input().split());print(' YNeos'[len(set([2 if i in [2] else 1 if i in [4,6,9,11] else 0 for i in [x,y]]))::2])