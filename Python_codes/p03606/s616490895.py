N = int(input())
l = [list(map(int,input().split())) for _ in range(N)]

person = 0
for i in range(N):
    a = l[i][1] - l[i][0] + 1
    person += a

print(person)

