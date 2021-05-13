from collections import deque
dictionary = set()
for making in range(int(input())) :
    action = input().split()
    if action[0] == 'insert' : dictionary.add(action[1])
    else : 
        if action[1] in dictionary : print('yes')
        else : print('no')