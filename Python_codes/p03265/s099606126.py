# B
x1, y1, x2, y2 = map(int, input().split())

od = [x1+y1-y2, y1-x1+x2]
oc = [x2-y2+y1, -x1+x2+y2]

od = map(str, list(od))
oc = map(str, list(oc))

print(' '.join(list(oc)) +' ' + ' '.join(list(od)))