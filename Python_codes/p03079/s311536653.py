import collections
print( 'Yes' if len(collections.Counter(map(int,input().split())).items()) == 1 else 'No' )