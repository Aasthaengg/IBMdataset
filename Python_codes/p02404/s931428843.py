figure = ''
height, width = [int(x) for x in input().split()]
while height or width:
    side = ('#' * width) + '\n'
    fill = '#' + ('.' * (width-2)) + '#\n'
    rect = side + (fill * (height-2)) + side
    figure += rect + '\n'
    height, width = [int(x) for x in input().split()]
  
print(figure[:-1])