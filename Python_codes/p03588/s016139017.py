import sys
input = sys.stdin.readline

N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]
AB.sort(key=lambda k: k[0], reverse=True)

print(AB[0][0]+AB[0][1])