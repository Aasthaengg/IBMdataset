def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

ABC = LI()
ABC.sort()
ans = 0

if (ABC[1] - ABC[0]) % 2 == 0:
    ans = (ABC[1] - ABC[0]) // 2 + ABC[2] - ABC[1]
    print(ans)

else:
    ABC[0] += 1
    ABC[2] += 1
    ans = ans = (ABC[1] - ABC[0]) // 2 + ABC[2] - ABC[1] + 1
    print(ans)