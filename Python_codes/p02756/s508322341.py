s = input()
q = int(input())
flip = 1
right_edge = list(s)
left_edge = []
for i in range(q):
    query = input()
    if query[0] == '1':
        flip *= -1
    else:
        if query[2] == '1':
            if flip == 1:
                left_edge.append(query[-1])
            else:
                right_edge.append(query[-1])
        else:
            if flip == 1:
                right_edge.append(query[-1])
            else:
                left_edge.append(query[-1])
left_edge = left_edge[::-1]
if flip == 1:
    print(''.join(left_edge + right_edge))
else:
    print(''.join(right_edge[::-1] + left_edge[::-1]))
        

