N = int(input())
T, A = map(int, input().split())
h = [abs(A-T+0.006*x) for x in map(int, input().split())]
print(h.index(min(h))+1)
