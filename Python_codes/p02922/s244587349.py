A, B = [int(x) for x in input().split()]

port = 1
plug = 0
while port < B:
    port += A - 1
    plug += 1

print(plug)
