# a, b = map(int, input().split())
li = list(map(int, input().split("/")))
print("Heisei" if li[1] <= 4 else "TBD")