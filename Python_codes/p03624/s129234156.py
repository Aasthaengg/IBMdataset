#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]
#a = [int(input()) for _ in range(n)]



s = input()

h = {}

alp = "abcdefghijklmnopqrstuvwxyz"

for i in alp:
    h[i] = 0

for i in s:
    h[i] += 1

#print(h)
for k,v in h.items():
    if (v == 0):
        print(k)
        exit()

print("None")

