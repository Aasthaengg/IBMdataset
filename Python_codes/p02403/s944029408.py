figure = ''
height, width = [int(x) for x in input().split()]
while height or width:
    side = ('#' * width) + '\n'
    rect = (side * height) + '\n'
    figure += rect
    height, width = [int(x) for x in input().split()]
 
print(figure[:-1])