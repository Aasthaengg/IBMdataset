import sys
H,W = map(int,input().split())
array = []
for I in range(H):
    array.append(list(map(str,input())))

if not (1 <= H <= 50 and 1 <= W <= 50):
    sys.exit()

result = [[0]*(W+2) for i in range((H+2))]
# test_result = [[0,1,2,3,4,5],[6,7,8,9,10,11],[12,13,14,15,16,17],[18,19,20,21,22,23]]
def input_result_array(x,y,result):
    result[x-1][y-1] += 1
    result[x-1][y] += 1
    result[x-1][y+1] += 1
    result[x][y-1] += 1
    result[x][y+1] += 1
    result[x+1][y-1] += 1
    result[x+1][y] += 1
    result[x+1][y+1] += 1
    return result

bomb_point = []
for I in range(H):
    for J in range(W):
        if array[I][J] == '#':
            bomb_point.append([I,J])
            result = input_result_array(I+1,J+1,result)

for I in range(len(bomb_point)):
    x,y=bomb_point[I]
    result[x+1][y+1] = '#'

str_result = ''
for I in [I[1:-1] for I in result[1:-1]]:
    for J in I:
        str_result += str(J)
    str_result += '\n'
print(str_result)