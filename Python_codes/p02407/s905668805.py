n = input()
a = [int(x) for x in input().split(" ")]
a.reverse()
print(" ".join([str(b) for b in a]))