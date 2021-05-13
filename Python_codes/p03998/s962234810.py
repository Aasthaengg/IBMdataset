dic = {}
dic['a'] = input()
dic['b'] = input()
dic['c'] = input()
turn = dic['a']
next = 'a'
while dic[next] !='':
    if turn[0] == 'a':
        dic[next] = turn[1:]
        turn = dic['a']
        next = 'a'
    elif turn[0] == 'b':
        dic[next] = turn[1:]
        turn = dic['b']
        next = 'b'
    else:
        dic[next] = turn[1:]
        turn = dic['c']
        next = 'c'
print(next.upper())