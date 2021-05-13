# ABC 121: A – White Cells
h_origin, w_origin = [int(s) for s in input().split()]
h, w = [int(s) for s in input().split()]
print((h_origin - h) * (w_origin - w))