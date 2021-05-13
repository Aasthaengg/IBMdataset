h1,m1,h2,m2,lens = [int(x) for x in input().split()]
available = (h2 * 60 + m2) - (h1 * 60 + m1)
answer = available - lens if available > lens else 0
print(answer)