import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

h,a = map(int, input().split())

# εγδΈγ
print((h+a-1)//a)
