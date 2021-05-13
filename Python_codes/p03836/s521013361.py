sx,sy,tx,ty = map(int,input().rstrip().split())
tmp_x = sx
tmp_y = sy

def print_route(sx,sy,tx,ty,goback,route):
    if goback == 'go':
        for i in range(tx-sx):
            route += 'R'
        for j in range(ty-sy):
            route += 'U'
    elif goback == 'back':
        for i in range(tx-sx):
            route += 'L'
        for j in range(ty-sy):
            route += 'D'
    else:
        pass
    return route
    
route = ""
route = print_route(sx,sy,tx,ty,'go',route)
route = print_route(sx,sy,tx,ty,'back',route)
route += 'D'
route = print_route(sx,sy-1,tx+1,ty,'go',route)
route += 'LU'
route = print_route(sx-1,sy,tx,ty+1,'back',route)
route += 'R'
print(route)