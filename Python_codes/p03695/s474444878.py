N = int(input())
A = [int(T) for T in input().split()]
Color = [T//400 for T in A if T<3200]
ColL = len(Color)
SetL = len(set(Color))
MIN = max(1,SetL)
MAX = SetL+(N-ColL)
print('{} {}'.format(MIN,MAX))