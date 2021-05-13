X,Y = (int(X,16) for X in input().split())
print((X<Y)*'<'+(X==Y)*'='+(X>Y)*'>')