ary = list(map(lambda n: int(n), input().split(" ")))

print("NO") if 2 * ary[1] - ary[0] - ary[2] else print("YES")