price=list(map(int,input().split()))

print(min(price)+sorted(price)[-2])