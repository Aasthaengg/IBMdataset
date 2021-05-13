from scipy import array, ndimage
H, _ = map(int, input().split())
print(ndimage.distance_transform_cdt(array([[c == "." for c in input()] for _ in range(H)], dtype=bool), metric="taxicab").max())
