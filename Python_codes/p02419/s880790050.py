w = input().strip()

t = []
while 1 :
    _t = input().strip().split(" ")
    if "END_OF_TEXT" in _t :
        break
    t.extend(_t)

print( sum([ i.lower()==w for i in t ] ) )
