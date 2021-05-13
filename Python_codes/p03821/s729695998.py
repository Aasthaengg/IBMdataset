n = int(input())

AB = []
for i in range(n):
    ab = list(map(int, input().split()))
    AB.append(ab)

ans = 0
for [a,b] in AB[::-1]:
    if (ans +a)%b == 0:
        pass
    else:
        quo = (ans +a)//b
        ans = (quo+1)*b - a

print(ans)
