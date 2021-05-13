n = int(input())
l = [0,0,0]
for i in range(n):
    a, b, c = map(int, input().split())
    l[0],l[1],l[2] = (max(l[1],l[2])+a, max(l[0],l[2])+b, max(l[0],l[1])+c)
print(max(l))