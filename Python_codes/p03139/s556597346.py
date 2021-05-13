N , A, B = list(map( int ,input().split() ))

# print(str(N) + ", " + str(A) + ", " + str(B))


maxab = min([A , B])

minab = max([A + B - N , 0] )

print(str(maxab) + " " + str(minab))
