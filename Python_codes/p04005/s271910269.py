ABC = list(map(int, input().split()))

ABC.sort()

ans = ABC[0] * ABC[1] * ((ABC[1] * ABC[1] * ABC[2]) % 2)

print(ans)